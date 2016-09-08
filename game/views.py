import os
import random

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import Card

def index(request):

	card_list = Card.objects.all()
	context = {'card_list': card_list}
	return render(request, 'game/index.html', context)


def generate_board(request):
	"""
	Read from word list and populate list
	"""
	WORD_LIST = []
	file_path = os.path.join(settings.PROJECT_ROOT, 'game/static/game/word_list.txt')
	with open(file_path, 'r') as f:
		for word in f:
			WORD_LIST.append(word.strip())

	"""
	Randomly sample for 25 words from word list
	"""
	random_list = random.sample(WORD_LIST, 25)

	"""
	Generate random list of colors
	"""
	#TODO

	"""
	Delete existing cards
	"""
	#TODO

	"""
	Create the new cards in database
	"""
	#TODO

	"""
	Redirect to board view
	"""
	#TODO

	return render(request, 'game/index.html', context)





