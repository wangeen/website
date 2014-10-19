# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response

class ViewHome(View):
    def get(self, request):
        # <view logic>
        return render_to_response('index.html')
    pass
