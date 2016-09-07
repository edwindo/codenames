from django.shortcuts import render
from django.http import HttpResponse

from .models import Card

def index(request):
	card_list = Card.objects.all()
	context = {'card_list': card_list}
	return render(request, 'game/index.html', context)





