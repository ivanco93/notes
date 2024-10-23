"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from notes.api.router import router_notes
import os

api_url = f'{os.environ.get("PROTOCOL", "http")}://{os.environ.get("BASE_URL", "localhost")}:{os.environ.get("PORT", "8000")}'
schema_view = get_schema_view(
   openapi.Info(
      title="Andesgt Notes API",
      default_version='v1',
      description="Notes API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ivandcastiblanco@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   url=api_url,
   #permission_classes=(permissions.AllowAny,),
   authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_notes.urls)),
]
