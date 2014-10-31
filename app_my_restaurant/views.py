# Create your views here.
# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext

class my_restaurant_home(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            #return render(request, 'my_restaurant/my_restaurant_login.html')
            print "is_authenticated false"
            return render_to_response('my_restaurant/my_restaurant_signin.html',  context_instance=RequestContext(request))
        else:
            print "is_authenticated true"
            #return render(request, 'my_restaurant/my_restaurant_edit_info.html')
            return render_to_response('my_restaurant/my_restaurant_edit_info.html',  context_instance=RequestContext(request))
    pass


class my_restaurant_info(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            print "is_authenticated false"
            return render_to_response('my_restaurant/my_restaurant_signin.html',  context_instance=RequestContext(request))
        else:
            print "is_authenticated true"
            #return render(request, 'my_restaurant/my_restaurant_edit_info.html')
            return render_to_response('my_restaurant/my_restaurant_edit_info.html',  context_instance=RequestContext(request))
    pass

class my_restaurant_home(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            #return render(request, 'my_restaurant/my_restaurant_login.html')
            print "is_authenticated false"
            return render_to_response('my_restaurant/my_restaurant_signin.html',  context_instance=RequestContext(request))
        else:
            print "is_authenticated true"
            #return render(request, 'my_restaurant/my_restaurant_edit_info.html')
            return render_to_response('my_restaurant/my_restaurant_edit_info.html',  context_instance=RequestContext(request))
    pass



class my_restaurant_home(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            #return render(request, 'my_restaurant/my_restaurant_login.html')
            print "is_authenticated false"
            return render_to_response('my_restaurant/my_restaurant_signin.html',  context_instance=RequestContext(request))
        else:
            print "is_authenticated true"
            #return render(request, 'my_restaurant/my_restaurant_edit_info.html')
            return render_to_response('my_restaurant/my_restaurant_edit_info.html',  context_instance=RequestContext(request))
    pass
