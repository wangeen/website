from django.conf.urls import patterns, include, url
from app_home.views import home_view
from app_my_restaurant.views import my_restaurant_home
from app_my_restaurant.views import my_restaurant_info
from app_my_restaurant.views import my_restaurant_menu
from app_my_restaurant.views import my_restaurant_desk
from app_my_restaurant.views import my_restaurant_update_name
from app_my_restaurant.views import my_restaurant_add_desk

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

    url(r'^my_restaurant/info$', my_restaurant_info, name="my_restaurant_info"),
    url(r'^my_restaurant/menu$', my_restaurant_menu, name="my_restaurant_menu"),
    url(r'^my_restaurant/desk$', my_restaurant_desk, name="my_restaurant_desk"),

    url(r'^my_restaurant/info/name_update$', my_restaurant_update_name, name="my_restaurant_update_name"),
    url(r'^my_restaurant/info/add_desk$', my_restaurant_add_desk, name="my_restaurant_add_desk"),

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
