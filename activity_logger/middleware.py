from .models import ActivityLog
from django.utils.timezone import now


class ActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = now()
        response = self.get_response(request)

        if request.user.is_authenticated:
            duration = (now() - start_time).total_seconds()
            ActivityLog.objects.create(
                user=request.user,
                method=request.method,
                path=request.path,
                action_type=self.get_action_type(request),
                status_code=response.status_code,
                ip_address=self.get_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT'),
                timestamp=now(),
                request_duration = duration
            )
        return response
    def get_action_type(self, request):
            if request.method == 'POST':
                return 'CREATE'
            elif request.method == 'PUT':
                return 'UPDATE'
            elif request.method == 'DELETE':
                return 'DELETE'
            return 'read'
        
    def get_ip(self, request):
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                return x_forwarded_for.split(',')[0]
            return request.META.get('REMOTE_ADDR')
        
    def get_request_data(self, request):
            if request.method == 'POST':
                    return request.POST.dict()
            return {}