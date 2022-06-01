"""MiniProject URL Configuration

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
from django.conf.urls import url
from appOne import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^register', views.register_request, name = 'register'),
    url(r'^login', views.user_login, name = 'login'),
    url(r'^logout', views.user_logout, name = 'logout'),
    url(r'^blog',views.blog,name='blog'),
    url(r'^delete/(?P<post_id>\d+)$',views.delete_view,name='delete_view'),
    url(r'^about', views.about, name = 'about'), 
    url(r'^update/(?P<id>\d+)$',views.update,name='update'),
    url(r'^readmore/(?P<id>\d+)$',views.readmore,name='readmore'),
    url(r'^comment/(?P<post_id>[0-9]+)/$',views.comment,name='comment'),
    url(r'^search/', views.search, name = 'search'),
    url(r'^welcome/', views.home, name = 'welcome'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
