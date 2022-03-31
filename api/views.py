from django.http import JsonResponse

from .models import Character


# Create your views here
def all_characters(request):
    all_characters = list(Character.objects.all().values('name', 'gender', 'birth_year', 'birth_planet', 'faction' ))
    print(all_characters)
    return JsonResponse({'request': all_characters})
