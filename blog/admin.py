from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'issueID', 'category', 'client', 'project_issue', 'project_finish', 'repairing_cost')
    list_filter = ('category', 'client', 'project_issue', 'project_finish')
    search_fields = ('name', 'issueID', 'description')

admin.site.register(BlogPost, BlogPostAdmin)

