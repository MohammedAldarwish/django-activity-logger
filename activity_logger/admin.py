from django.contrib import admin

from .models import ActivityLog

class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'method', 'path', 'action_type', 'status_code', 'ip_address', 'user_agent', 'timestamp', 'request_duration')  # إضافة الـ timestamp هنا
    list_filter = ('timestamp',)

admin.site.register(ActivityLog, ActivityLogAdmin)