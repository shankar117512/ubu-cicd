# apps/core/views.py
from django.http import JsonResponse
from django.db import connection
 
def health_check(request):
    checks = {}
    try:
        connection.ensure_connection()
        checks['database'] = 'ok'
    except Exception as e:
        checks['database'] = str(e)
    status = 200 if checks.get('database') == 'ok' else 503
    return JsonResponse({'status': 'ok' if status == 200 else 'error',
                         'checks': checks}, status=status)
 
# myproject/urls.py — add this
from apps.core.views import health_check
urlpatterns = [
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
]
