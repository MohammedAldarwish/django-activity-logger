from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=200)
    action_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=512, null=True, blank=True)
    request_duration  = models.FloatField()


        
    def __str__(self):
        return f"{self.user} - {self.action_type} - {self.action_type}"