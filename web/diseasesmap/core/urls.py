"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import account, diseases, index,login,logout,dashboard,about,contact, notifications, populate, usertable, about_restrict, contact_restrict

urlpatterns = [
    path('django/', admin.site.urls),
    path('', dashboard),
    path('about/', about_restrict),
    path('contact/', contact_restrict),
    path('login/', login),
    path('logout/', logout),
    path('admin/', index),
    path('admin/about/', about),
    path('admin/contact/', contact),
    path('admin/notifications/', notifications),
    path('admin/account/', account),
    path('admin/usertable/', usertable),
    re_path(r'^admin/usertable/(?P<pathId>[/\w]+)/$', usertable),
    path('admin/diseases/', diseases),
    path('db/',include('server.urls')),

    #DANGEROUS PATH
    path('admin/db/populate', populate)
]
