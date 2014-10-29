from django.conf.urls import patterns, include, url
from app_home.views import home_view
from app_my_restaurant.views import my_restaurant_home

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
    url(r'^my_restaurant/$', my_restaurant_home.as_view(), name="my_restaurant_home"),
    url(r'^my_restaurant/login$',  'django.contrib.auth.views.login', {'template_name':'my_restaurant/my_restaurant_signin.html'}, name='login'),
    url(r'^my_restaurant/logout$',  'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^my_restaurant/signup$', 'app_auth.views.signup_view', name='signup'),


    (r'^resetpassword/passwordsent/$','django.contrib.auth.views.password_reset_done'),
    (r'^resetpassword/$','django.contrib.auth.views.password_reset'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$','django.contrib.auth.views.password_reset_complete'),

    # debug code
    url(r'^$', home_view.as_view(), name='feeds'),
    url(r'^$', home_view.as_view(), name='articles'),
    url(r'^$', home_view.as_view(), name='questions'),
    url(r'^$', home_view.as_view(), name='network'),
    url(r'^$', home_view.as_view(), name='search'),
    url(r'^$', home_view.as_view(), name='profile'),
)
