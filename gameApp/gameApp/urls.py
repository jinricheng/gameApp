from django.conf.urls import patterns, include, url
from igame.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    # url(r'^gameApp/', include('gameApp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'), 
    url('^shop/$',shopsection,name='shop'),
    url('^(\w+)/shop/$',shopsection_JsonXml,name='shopJsonXml'),	
    url('^producer/$',producersection,name='producer'),
    url('^(\w+)/producer/$',producersection_JsonXml,name='producerJsonXml'),
    url('^game/$',gamesection,name='Game'),
    url('^(\w+)/game/$',gamesection_JsonXml,name='GameJsonXml'),	
    url('^shop/(\d{1,2})/$',shopDetail,name='shopdetail'),	
    url('^game/(\d{1,2})/$',gameDetail,name='gamedetail'),
    url('^producer/(\d{1,2})/$',producerDetail,name='producerDetail'),
)
