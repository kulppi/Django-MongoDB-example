from django.conf.urls.defaults import *

from movies import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^movies/', include('movies.urls')),
    url(r'^admin/', include(admin.site.urls)),
)




