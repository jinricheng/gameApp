# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render_to_response
from django.template import loader,Context, Template
from django.template.loader import get_template
from igame.models import Game,Shop,Producer,gameReview
import json
from django.utils import simplejson



def mainpage(request):
	
	template = get_template('mainpage.html')
	
	variables = Context({
			'titlehead': 'Game Search App',
			'pagetitle':'Welcome to the Game Search Application',
			'contentbody':'',
			'game':'games',
			'shop':'shops',
			'producer':'producers',
			'user': request.user
	})
	output = template.render(variables)
	return HttpResponse(output)

class gameDetail(DetailView):
	model = Game
	template_name = 'gameDetail.html'

	def get_context_data(self,**kwargs):
	    context = super(gameDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    context['producer'] = Producer.objects.all()
	    return context
