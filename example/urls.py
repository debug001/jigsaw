from django.conf.urls.defaults import *

urlpatterns = patterns('example',
    url(r'^line/$', 'main.line'),
    url(r'^pie/$', 'main.pie'),
    url(r'^map/$', 'main.map'),
    url(r'^test/$', 'main.test'),
)
