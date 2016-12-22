from django.conf.urls import url

from restapp import views

urlpatterns = [
    url(r'^mymodels/$', views.MyModelList, name='mymodel_list'),
    url(r'^make/(?P<pk>[0-9]+)/$', views.MyModelDetail,name='mymodel_detail'),
]
