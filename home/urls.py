from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('termsCondition', views.termsCondition, name='terms'),
    path('privacyPolicy', views.privacyPolicy, name='privacy'),
    path('subscription', views.subscription, name='subscription'),
   
   
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


