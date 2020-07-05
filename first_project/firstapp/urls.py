
from django.conf.urls import url, include
from firstapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

]