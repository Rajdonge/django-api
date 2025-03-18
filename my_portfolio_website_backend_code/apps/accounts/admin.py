from django.contrib import admin
from . models import User, Logo, Banner, SocialMedia, CV, Project, Enquiry

class AdminUser(admin.ModelAdmin):
    list_display = ['id', 'email']

admin.site.register(User, AdminUser)

class LogoAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Logo, LogoAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Banner, BannerAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(SocialMedia, SocialMediaAdmin)

class CVAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(CV, CVAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_title']
admin.site.register(Project, ProjectAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'visitor_email']
admin.site.register(Enquiry, EnquiryAdmin)