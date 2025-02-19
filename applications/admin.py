from django.contrib import admin
from .models import JobApplication

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    actions = ['mark_as_shortlisted', 'mark_as_rejected']

    def mark_as_shortlisted(self, request, queryset):
        queryset.update(status='Shortlisted')
    mark_as_shortlisted.short_description = 'Mark selected applications as Shortlisted'

    def mark_as_rejected(self, request, queryset):
        queryset.update(status='Rejected')
    mark_as_rejected.short_description = 'Mark selected applications as Rejected'

admin.site.register(JobApplication, JobApplicationAdmin)

