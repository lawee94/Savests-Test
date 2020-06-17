from django.contrib import admin
from django.urls import path
from myapp.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin_site.urls), 
]
