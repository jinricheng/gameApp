# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader,Context, Template
from django.template.loader import get_template
from igame.models import Game,Shop,Producer
import json
from django.utils import simplejson

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
	'''return HttpResponse(output,mimetype=application/xml)'''

def gamesection_JsonXml(request,types):
	try:
		games = Game.objects.all()
		if types == 'json':
			list_games = []
			for game in games:
				g = {"id":game.id,"name":game.name}
				list_games.append(g)
				games = {"All Games":list_games}
			return HttpResponse(json.dumps(games))
		elif types == 'xml':
			variables = Context({
						'games':games
						})
			load = loader.get_template('gamesection.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		raise Http404('Game Not Found')



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

def shopsection_JsonXml(request,types):
	try:
		shops = Shop.objects.all()
		if types == 'json':
			list_shops = []
			for shop in shops:
				g = {"id":shop.id,"name":shop.name}
				list_shops.append(g)
				shops = {"All Shops":list_shops}
			return HttpResponse(json.dumps(shops))
		elif types == 'xml':
			variables = Context({
						'shops':shops
						})
			load = loader.get_template('shopsection.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		raise Http404('Shop Not Found')

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


def producersection_JsonXml(request,types):
	try:
		producers = Producer.objects.all()
		if types == 'json':
			list_producers = []
			for producer in producers:
				g = {"id":producer.id,"name":producer.name}
				list_producers.append(g)
				producers = {"All Producers":list_producers}
			return HttpResponse(json.dumps(producers))
		elif types == 'xml':
			variables = Context({
						'producers':producers
						})
			load = loader.get_template('producersection.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		return Http404('No producers Found')

def shopDetail(request,shopid):
	try:
        	shop = Shop.objects.get(id=shopid)
		
	except:
		raise Http404('shop Not Found')
	games = shop.game_set.all()
	
	return render_to_response('shopDetail.html',{'shop':shop,'games':games,})

def shopDetail_JsonXml(request,types,shopid):
	try:
		shop = Shop.objects.get(id = shopid)
		if types == 'json':
			g = {"id":shop.id,"name":shop.name,"address":shop.address}
			return HttpResponse(json.dumps(g))
		elif types == 'xml':
			variables = Context({
						'shop':shop
					})
			load = loader.get_template('shopDetail.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		raise Http404('shop Not Found')
	
		
def gameDetail(request,gameid):
	try:
		game = Game.objects.get(id = gameid)
		
	except:
		raise Http404('Game Not Found')
	producer = Producer.objects.get(name = str(game.producedBy))
	shops = game.soldBy.all()
	return render_to_response('gameDetail.html',{'game':game,'shops':shops,'producer':producer,})


def gameDetail_JsonXml(request,types,gameid):
	try:
		game = Game.objects.get(id = gameid)
		if types == 'json':
			g = {"Id":game.id,"Name":game.name,"PublishYear":game.publishYear}
			return HttpResponse(json.dumps(g))
		elif types == 'xml':
			variables = Context({
						'game':game
					})
			load = loader.get_template('gameDetail.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		Http404('error')


def producerDetail(request,producerid):
	try:
        	producer = Producer.objects.get(id = producerid)
		
	except:
		raise Http404('shop Not Found')
	games = producer.game_set.all()
	return render_to_response('producerDetail.html',{'producer':producer,'games':games})

def producerDetail_JsonXml(request,types,producerid):
	try:
		producer = Producer.objects.get(id = producerid)
		if types == 'json':
			g = {"Id":producer.id,"Name":producer.name,"Address":producer.address}
			return HttpResponse(json.dumps(g))
		elif types == 'xml':
			variables = Context({
						'producer':producer
					})
			load = loader.get_template('producerDetail.xml')
			context = Context(variables)
			return HttpResponse(load.render(context),mimetype="application/xml")
	except:
		Http404('error')

