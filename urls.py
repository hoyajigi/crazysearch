from django.conf.urls.defaults import *
from crazysearch.views import *
import os.path
from django.conf.urls.defaults import *

static=os.path.join(os.path.dirname(__file__),'static')

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^me2echelon/', include('me2echelon.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),


	(r'^$',main_page),
	(r'^crazysearch/.*$',search),
	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':static}),
)
