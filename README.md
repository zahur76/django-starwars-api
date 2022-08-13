# STARWARS API 

Star wars api making use of django restframework. Frontend programmed with React on different domain.

Also makes use of JWT to access api views.

Uses allauth and dj-rest-auth for login and registration purposes. Modifies dj urls and views to make use of allauth.

ConfirmEmailView modified in venv dj_rest_allauth registration urls to direct to allauth views to return response

### Tecnologies used

* Django
* Django Rest Framework - API requests
* Simple JWT - for token authentication (https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
    Used for Token Authentication bypassing DRF basic token authentication.
* dj-rest-auth - for authentication with DRF (https://dj-rest-auth.readthedocs.io/en/latest/introduction.html)
    used with Simple JWT to allow access to views