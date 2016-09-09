from django.conf.urls import url

from . import views

urlpatterns = [ 
	url(r'^$', views.index, name='index'),
	url(r'^generate_board/$', views.generate_board, name='generate_board')
]