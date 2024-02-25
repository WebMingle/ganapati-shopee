from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role','website_link', 'facebook_link', 'instagram_link', 'twitter_link', 'linkedin_link')
    list_filter = ('role',)

admin.site.register(Member, MemberAdmin)

