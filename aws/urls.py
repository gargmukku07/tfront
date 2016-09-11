from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

#urlpatterns = [
#	url(r'^$', views.index, name='index'),
#]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello/', views.hello, name='hello'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]
