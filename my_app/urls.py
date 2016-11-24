from django.conf.urls import url
from my_app import views

urlpatterns = [
    #url(r'^login/', views.login, name='login'),
    url(r'^service/(?P<service_id>\d+)/$', views.service, name='service'),
    url(r'^$', views.index, name='index'),
]