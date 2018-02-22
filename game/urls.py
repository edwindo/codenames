from django.conf.urls import url

from . import views

urlpatterns = [ 
	url(r'^$', views.index, name='index'),
	url(r'^generate_board/$', views.generate_board, name='generate_board'),
	url(r'^toggle_card/(?P<card_id>[0-9]+)/$', views.toggle_card, name='toggle_card'),
	url(r'^codemaster/$', views.codemaster, name='codemaster'),
	url(r'^build/$', views.build, name='build'),
]