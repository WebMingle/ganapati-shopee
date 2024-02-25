from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'link' , 'comment')
    list_filter = ('role',)

admin.site.register(Post, PostAdmin)

