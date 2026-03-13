from django.http import JsonResponse
from django.urls import path
from django.contrib import admin


def health_check(request):
    return JsonResponse({"status": "ok"})
