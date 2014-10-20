from django.conf.urls import patterns, include, url
from home.views import ViewHome

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ViewHome.as_view(), name='home'),
    url(r'^login',  'django.contrib.auth.views.login', {'template_name':'index.html'}, name='login'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)