# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext

class home_view(View):
    def get(self, request):
        # <view logic>
        print "get home_view"
        response_class_instance = render_to_response('index.html',  context_instance=RequestContext(request))
        print "finish home_view"
        return response_class_instance
    pass
