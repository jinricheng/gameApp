# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template
from igame.models import Game,Shop,Producer


def mainpage(request):
	
	template = get_template('mainpage.html')
	
	variables = Context({
			'titlehead': 'Game Search App',
			'pagetitle':'Welcome to the Game Search Application',
			'contentbody':'',
			'game':'game',
			'shop':'shop',
			'producer':'producer',
			'user': request.user
	})
	output = template.render(variables)
	return HttpResponse(output)


def gamesection(request):
	try:
		games = Game.objects.all()
	except:
		raise Http404('gamesection not found.')
	template = get_template('gamesection.html')
	variables = Context({
		'games':games,
	})
	
	output = template.render(variables)
	return HttpResponse(output)



def shopsection(request):	
	try:
		shops = Shop.objects.all()
	except:
		raise Http404('shopsection not found.')
	template = get_template('shopsection.html')
	variables = Context({
		'shops':shops,
	})
	
	output = template.render(variables)
	return HttpResponse(output)


def producersection(request):
	try:
		producers = Producer.objects.all()
	except:
		raise Http404('shop Not Found')
	template = get_template('producersection.html')
	variables = Context({
		'producers':producers,
	})
	
	output = template.render(variables)
	return HttpResponse(output)

def shopGame(request,shopname):
	try:
        	shop = Shop.objects.get(name=shopname)
		
	except:
		raise Http404('shop Not Found')

	return render_to_response('shopGame.html',{'shop':shop,})


def gameDetail(request,gamename):
	try:
		game = Game.objects.get(name = gamename)
	except:
		raise Http404('shop Not Found')

	return render_to_response('gameDetail.html',{'game':game,})
