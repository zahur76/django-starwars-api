# STARWARS API 

Star wars api making use of django restframework. Frontend programmed with React on different domain.

Also makes use of JWT to access api views.

Uses allauth and dj-rest-auth for login and registration purposes. Modifies dj urls and views to make use of allauth.

- need to update:
    - confirm_email in allauth account
    - update url in dj-rest-auth registration ```account-confirm-email/``` to point to ConfirmEmailView

ConfirmEmailView modified in venv dj_rest_allauth registration urls to direct to allauth views to return response

### Tecnologies used

* Django
* Django Rest Framework - API requests
* Simple JWT - for token authentication (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
    Used for Token Authentication bypassing DRF basic token authentication.
* dj-rest-auth - for authentication with DRF (https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
    used with Simple JWT to allow access to views


### Modifications

* change allauth registration confirm email view to redirect to react front end page.


### Social Account Login

* create app

    ```django-admin startapp social-login ```

    - update Settings app

        ``` INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'corsheaders',
            "rest_framework",
            'rest_framework.authtoken',
            'dj_rest_auth',
            'api',
            'socia;_login',

            'django.contrib.sites',
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'dj_rest_auth.registration',
            'allauth.socialaccount.providers.google',
        ] ```
    
* create view in social_login/views.py
    
    ```
        from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
        from dj_rest_auth.registration.views import SocialLoginView
        from allauth.socialaccount.providers.oauth2.client import OAuth2Client
        from django.conf import settings

        class GoogleLogin(SocialLoginView):
            authentication_classes = [] # disable authentication
            adapter_class = GoogleOAuth2Adapter
            callback_url = "http://localhost:3000"
            client_class = OAuth2Client
    ```

* add url to starwars_api/urls.py

    ``` path('social_login/google/', GoogleLogin.as_view(), name='google_login') ```

    - login will provide get request requiring token obtaned from api request to google

* update settings.py 

    ```
        SOCIALACCOUNT_PROVIDERS = {
            'google': {
               'SCOPE': [
                    'profile',
                    'email',
               ],
                'AUTH_PARAMS': {
                    'access_type': 'online',
                }
            }
        }
        
        # Disable email verification since this is just a test.
        # If you want to enable it, you'll need to configure django-allauth's email confirmation pages
        SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
        SOCIALACCOUNT_EMAIL_REQUIRED = False
        
        REST_USE_JWT = True
        
        SITE_ID = 1
        
        from datetime import timedelta
        
        SIMPLE_JWT = {
            'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
            'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
            'ROTATE_REFRESH_TOKENS': True, # IMPORTANT
            'BLACKLIST_AFTER_ROTATION': True, # IMPORTANT
            'UPDATE_LAST_LOGIN': True,
        }
        
        MIDDLEWARE = [
            "corsheaders.middleware.CorsMiddleware",
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
        
        CORS_ORIGIN_ALLOW_ALL = True
        
        # Rest Settings
        REST_FRAMEWORK = {
            "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
            "DEFAULT_AUTHENTICATION_CLASSES": (
                "rest_framework.authentication.BasicAuthentication",
                "rest_framework.authentication.SessionAuthentication",
                "dj_rest_auth.utils.JWTCookieAuthentication",
            ),
        }
    ```

* set-up google auth Front end
    
    - install ``` npm install react-google-login --legacy-peer-dep ``` & ``` npm install --save gapi-script ```

    - add google sign in form to obtain code and token using react-google-login

    - setup social application with client id and key obtained from google api console. Remember to add site to settings.

    - send token obtained when signing in to http://127.0.0.1:8000/social_login/google/ url. 





