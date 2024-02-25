from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'phonenumber', 'subject')
    list_display_links = ('id', 'fullname')
    search_fields = ('fullname', 'email', 'phonenumber', 'subject')
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)

