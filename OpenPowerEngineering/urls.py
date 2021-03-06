"""OpenPowerEngineering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
import power.urls
import computer.urls, blog.urls
from django.conf.urls.static import static
from yournotes.views import note_view,note_save
from accounts.views import login_view,logout_view,register_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(power.urls)),
    url(r'^computing/',include(computer.urls)),
    url(r'^blog/',include(blog.urls), name='blog'),
    url(r'^login/', login_view , name='login'),
    url(r'^logout/',logout_view, name='logout'),
    url(r'^register/',register_view, name='register'),
    url(r'^notes/',note_view, name='yournotes'),
    url(r'^uploadnotes/',note_save, name='noteupload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)