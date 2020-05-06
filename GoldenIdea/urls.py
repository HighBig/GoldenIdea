"""GoldenIdea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import os
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from ideas.views import list_view

urlpatterns = [
    path('', list_view, name='list'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('ideas/', include('ideas.urls', namespace='ideas')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.LOGS_URL, document_root=settings.LOGS_DIR)
    LETSENCRYPTIT_URL = '/.well-known/'
    LETSENCRYPTIT_ROOT = os.path.join(settings.BASE_DIR, ".well-known")
    urlpatterns += static(LETSENCRYPTIT_URL, document_root=LETSENCRYPTIT_ROOT)