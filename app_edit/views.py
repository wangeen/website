# Create your views here.
# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext

class edit_view(View):
    def get(self, request):
        # <view logic>
        print "get edit_view"
        return render_to_response('edit.html',  context_instance=RequestContext(request))
    pass
