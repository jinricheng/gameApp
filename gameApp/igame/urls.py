from django.conf.urls import patterns, include, url
from django.utils import timezone
from django.views.generic import DetailView,ListView,UpdateView
from igame.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from igame.models import Shop,Game,Producer
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
  
    # url(r'^gameApp/', include('gameApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',ListView.as_view(
	queryset=Game.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
	context_object_name='Game_List',
	template_name='firstPage.html'),
	name = 'game_list'),
    
    url(r'^gamesection/$',
	ListView.as_view(
	queryset=Game.objects.all(),
	context_object_name='Game_List',
	template_name='gamesection.html'),
	name = 'game_section'),

    url(r'^shopsection/$',
	ListView.as_view(
	queryset=Shop.objects.all(),
	context_object_name='Shop_List',
	template_name='shopsection.html'),
	name = 'shop_section'),

    url(r'^producersection/$',
	ListView.as_view(
	queryset=Producer.objects.all(),
	context_object_name='Producer_List',
	template_name='producersection.html'),
	name = 'producer_section'),

    url(r'^games/(?P<pk>\d+)/$',
	gameDetail.as_view(),
	name = 'game_detail'),

    url(r'^shops/(?P<pk>\d+)/$',
	shopDetail.as_view(),
	name = 'shop_detail'),

    url(r'^producers/(?P<pk>\d+)/$',
	producerDetail.as_view(),
	name = 'producer_detail'),
 
    url(r'^games/create/$',
	gameCreate.as_view(),
	name = 'game_create'),

    url(r'^shops/create/$',
	shopCreate.as_view(),
	name = 'shop_create'),

    url(r'^producers/create/$',
	producerCreate.as_view(),
	name = 'producer_create'),

    url(r'^games/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=Game, form_class=gameForm),
        name='game_edit'),
    
    url(r'^shops/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=Shop, form_class=shopForm),
        name='shop_edit'),

    url(r'^games/(?P<pk>\d+)/reviews/create/$',
        'igame.views.review',
        name='review_create'),
    
    url(r'^producers/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=Producer, form_class=producerForm),
        name='producer_edit'),

    url(r'^games/(?P<pk>\d+)/delete/$',
        gameDelete.as_view(success_url=("/igame/")),
        name='game_delete'),

    url(r'^shops/(?P<pk>\d+)/delete/$',
        shopDelete.as_view(success_url=("/igame/")),
        name='shop_delete'),

    url(r'^producers/(?P<pk>\d+)/delete/$',
        producerDelete.as_view(success_url=("/igame/")),
        name='producer_delete'),
)


#RESTful API
urlpatterns += patterns('',
    url(r'^api/games/$', APIGameList.as_view(), name='game-list'),
    url(r'^api/games/(?P<pk>\d+)/$', APIGameDetail.as_view(), name='game-detail'),
    url(r'^api/shops/$', login_required(APIShopList.as_view()), name='shop-list'),
    url(r'^api/shops/(?P<pk>\d+)/$', APIShopDetail.as_view(), name='shop-detail'),
    url(r'^api/producers/$', login_required(APIProducerList.as_view()), name='producer-list'),
    url(r'^api/producers/(?P<pk>\d+)/$', APIProducerDetail.as_view(), name='producer-detail'),
    url(r'^api/gamereviews/$', APIGameReviewList.as_view(), name='gamereview-list'),
    url(r'^api/gamereviews/(?P<pk>\d+)/$', APIGameReviewDetail.as_view(), name='gamereview-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json', 'xml'])
