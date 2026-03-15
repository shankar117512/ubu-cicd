from django.http import JsonRespone

def health_check(request):
    return JsonResponse({"status": "ok"})
