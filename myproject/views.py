from django.http import JsonResponse


def home(request):
    return JsonResponse({"message": "Django CI/CD Deployment Successfully!"})
    

def health_view(request):
    return JsonResponse({"status": "ok"})
