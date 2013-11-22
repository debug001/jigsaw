from django.conf.urls import patterns, include, url
from django.conf import settings



urlpatterns = patterns('',
    url(r'^example/', include('example.urls')),
    url(r'^ajax/', include('ajax.urls')),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/css"}),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/js"}),
    url(r'^echarts/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/echarts"}),
    url(r'^zrender/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DIR+"/zrender"}),
)
