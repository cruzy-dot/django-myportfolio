from django.contrib import admin
from .models import Project, Skill, ContactMessage
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Assuming you have a 'created_at' field
    search_fields = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # If you have 'submitted_at'
    search_fields = ('name', 'email', 'message')

admin.site.site_header = "Admin"
admin.site.site_title = "Portfolio Admin Portal"
admin.site.index_title = "Welcome to My Portfolio Dashboard"