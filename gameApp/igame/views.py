# Create your views here.
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core import urlresolvers
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView,DeleteView
from django.views.generic.edit import CreateView,UpdateView
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from igame.models import Game,Shop,Producer,gameReview
from forms import gameForm, shopForm,producerForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


class gameDetail(DetailView):
	model = Game
	template_name = 'gameDetail.html'

	def get_context_data(self,**kwargs):
	    context = super(gameDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    
	    return context


class shopDetail(DetailView):
	model = Shop
	template_name = 'shopDetail.html'

	def get_context_data(self,**kwargs):
	    context = super(shopDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    return context


class producerDetail(DetailView):
	model = Producer
	template_name = 'producerDetail.html'

	def get_context_data(self,**kwargs):
	    context = super(producerDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    return context

class gameSectionDetail(DetailView):
	model = Game
	template_name = 'gamesection.html'

	def get_context_data(self,**kwargs):
	    context = super(gameSectionDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    
	    return context

class shopSectionDetail(DetailView):
	model = Game
	template_name = 'shopsection.html'

	def get_context_data(self,**kwargs):
	    context = super(shopSectionDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    
	    return context


class producerSectionDetail(DetailView):
	model = Game
	template_name = 'producersection.html'

	def get_context_data(self,**kwargs):
	    context = super(shopSectionDetail,self).get_context_data(**kwargs)
	    context['RATING_CHOICES'] = gameReview.RATING_CHOICES
	    
	    return context



class gameCreate(LoginRequiredMixin, CreateView):
	model = Game
	template_name = 'form.html'
	form_class = gameForm

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(gameCreate,self).form_valid(form)


class shopCreate(LoginRequiredMixin, CreateView):
	model = Shop
	template_name = 'form.html'
	form_class = shopForm

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(shopCreate,self).form_valid(form)


class producerCreate(LoginRequiredMixin, CreateView):
	model = Producer
	template_name = 'form.html'
	form_class = producerForm

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(producerCreate,self).form_valid(form)

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    	template_name = 'form.html'



class gameDelete(DeleteView):
    	model = Game
	template_name = 'gameDelete.html'



class shopDelete(DeleteView):
    	model = Shop
	template_name = 'shopDelete.html'


class producerDelete(DeleteView):
    	model = Producer
	template_name = 'producerDelete.html'

@login_required()
def review(request,pk):
	game = get_object_or_404(Game, pk=pk)
    	new_review = gameReview(
        	rating=request.POST['rating'],
        	comment=request.POST['comment'],
       		user=request.user,
        	game=game)
    	new_review.save()
    	return HttpResponseRedirect(urlresolvers.reverse('igame:game_detail', args=(game.id,)))
	

