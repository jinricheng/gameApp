from django.conf.urls import patterns, include, url
from django.utils import timezone
from django.views.generic import DetailView,ListView,UpdateView
from igame.views import *
from igame.models import Shop,Game,Producer
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
  
    # url(r'^gameApp/', include('gameApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'), 
   
    url(r'^$',ListView.as_view(
	queryset=Game.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
	context_object_name='Game_List',
	template_name='gamesection.html'),
	name = 'game_list'),
   
    url(r'^games/(?P<pk>\d+)/$',
	gameDetail.as_view(),
	name = 'game_detail'),
)
