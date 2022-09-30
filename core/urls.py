"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import render

from users.views import UserViewSetCustom

def main_view(request):
	return render(request,"index.html")


from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("users", UserViewSetCustom)
User = get_user_model()



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/",include("api.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("",main_view),
    path("auth/", include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += [ re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]