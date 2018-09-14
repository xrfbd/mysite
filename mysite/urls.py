"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^newarticle/$', views.edit_article),

    url(r'^login/$', views.login),
    url(r'^$', views.login,name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^edit_article/$', views.edit_article, name='edit_article'),
    url(r'^article_list/$', views.article_list, name='article_list'),
]
