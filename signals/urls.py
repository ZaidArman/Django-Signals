from django.contrib import admin
from django.urls import path, include
from django.views import View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signalApp.urls')),
]
