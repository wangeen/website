from django.conf.urls import patterns, include, url
from app_home.views import home_view
from app_edit.views import edit_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home_view.as_view(), name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # edit menu
    url(r'^edit/$', edit_view.as_view(), name="edit"),
    url(r'^edit/login$',  'django.contrib.auth.views.login', {'template_name':'index.html'}, name='login'),
    url(r'^edit/logout$',  'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^edit/signup$', 'app_auth.views.signup_view', name='signup'),


    # debug code
    url(r'^$', home_view.as_view(), name='feeds'),
    url(r'^$', home_view.as_view(), name='articles'),
    url(r'^$', home_view.as_view(), name='questions'),
    url(r'^$', home_view.as_view(), name='network'),
    url(r'^$', home_view.as_view(), name='search'),
    url(r'^$', home_view.as_view(), name='profile'),
)
