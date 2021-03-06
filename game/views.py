import os
import random

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse


from .models import Card

def index(request):

	card_list = Card.objects.all()
	red_count = 0
	blue_count = 0
	for card in card_list:
		if card.color == "red" and not card.visibility:
			red_count += 1
		if card.color == "blue" and not card.visibility:
			blue_count += 1
		if card.color == "black" and card.visibility:
			return render(request, 'game/gg.html')
	context = {'card_list': card_list, 'red_count': red_count, 'blue_count': blue_count}
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
	random_color_list = []
	for n in range(0,8):
		random_color_list.append("blue")
	for n in range(0,9):
		random_color_list.append("red")
	for n in range(0,7):
		random_color_list.append("yellow")
	random_color_list.append("black")

	random.shuffle(random_color_list)

	"""
	Delete existing cards
	"""
	Card.objects.all().delete()

	"""
	Create the new cards in database
	"""
	for i in range(0,25):
		card = Card(word = random_list[i], color = random_color_list[i], visibility = False)
		card.save()

	"""
	Redirect to board view
	"""
	return HttpResponseRedirect(reverse('index'))

def toggle_card(request, card_id):
	card = Card.objects.get(pk=card_id)
	card.visibility = True
	card.save()
	return HttpResponseRedirect(reverse('index'))

def codemaster(request):
	card_list = Card.objects.all()
	red_list = []
	blue_list = []
	yellow_list = []
	already_found = []
	
	for card in card_list:
		if card.color == "red" and not card.visibility:
			red_list.append(card)
		elif card.color == "blue" and not card.visibility:
			blue_list.append(card)
		elif card.color == "yellow"and not card.visibility:
			yellow_list.append(card)
		elif card.color == "black":
			assassinCard = card
		else:
			already_found.append(card)


	context = {'red_list':red_list, 'blue_list':blue_list, 'yellow_list':yellow_list, 'assassinCard':assassinCard, 'already_found':already_found}
	return render(request, 'game/codemaster.html', context)

def build(request):
	return render(request, 'game/build.html')











