# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext

class ViewHome(View):
    def get(self, request):
        # <view logic>
        print "ViewHome"
        return render_to_response('index.html',  context_instance=RequestContext(request))
    pass
