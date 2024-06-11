"""grace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from category.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('3D-модели/', models,  name='models'),
    path('Съемки 360°/', panarams,  name='panarama'),
    path('Видео с дрона/', dron,  name='dron'),
    path('AR разработка/', ar,  name='ar'),
    path('Фото-видео съемка/', foto,  name='foto'),
    path('VR разработка/', vr,  name='vr'),
    path('UI/UX дизайн/', ux,  name='ux'),
]
