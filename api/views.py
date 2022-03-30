from django.http import JsonResponse


# Create your views here
def all_characters(request):
    return JsonResponse({'name': 'zahur'})
