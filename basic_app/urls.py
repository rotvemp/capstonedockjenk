from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns= [

    url(r'^$',views.AuthorList.as_view(),name='list'),
    url(r'^delete/(?P<pk>\d+)/$', views.AuthorDelete.as_view(),name = 'delete' ),


]
