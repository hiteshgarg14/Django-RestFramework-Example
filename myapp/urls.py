from django.conf.urls import url

from myapp import views

app_name = 'myapp'
urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete,name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update,name='update'),
    url(r'^search/$', views.search,name='search'),
]
