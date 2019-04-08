"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('', include('core.urls')),

    path('users/', include('users.urls')), # user path for all-auth
    #path('users/', include('django.contrib.auth.urls')), # user path for default all-auth
    path('accounts/', include('allauth.urls')), # added for all-auth, replaces line above

    path('kids/', include('kids.urls')),         #added for the kids event tracker
    path('shopping/', include('shopping.urls')), #added for the shopping list
    path('finances/', include('finances.urls')), #add for the financial tracker

    path('admin/', admin.site.urls),
]
