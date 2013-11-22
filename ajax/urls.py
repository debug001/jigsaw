from django.conf.urls.defaults import *

urlpatterns = patterns('ajax',
    url(r'^line/$', 'main.line'),
    url(r'^pie/$', 'main.pie'),
    url(r'^map/$', 'main.map')
)
