# Create your views here.
# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_my_restaurant.models import my_restaurant_info_model

class my_restaurant_home(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            #return render(request, 'my_restaurant/my_restaurant_login.html')
            print "is_authenticated false"
            return render_to_response('my_restaurant/my_restaurant_signin.html',  context_instance=RequestContext(request))
        else:
            return my_restaurant_info(request)
    pass

@login_required
def my_restaurant_info(request):
    form = restaurant_name_form()
    obj, created = my_restaurant_info_model.objects.get_or_create(user=request.user)
    print obj
    name = obj.restaurant_name
    print "xxxxxx",name, created
    return render(request,'my_restaurant/my_restaurant_edit_info.html',{
        'name_form':form,
        'current_name':name
    })

@login_required
def my_restaurant_menu(request):
    return render_to_response('my_restaurant/my_restaurant_edit_menu.html',  context_instance=RequestContext(request))

@login_required
def my_restaurant_desk(request):
    return render_to_response('my_restaurant/my_restaurant_edit_desk.html',  context_instance=RequestContext(request))

from app_my_restaurant.forms import restaurant_name_form
@login_required
def my_restaurant_update_name(request):
    if request.method == 'POST':
        form = restaurant_name_form(request.POST)
        print request.user
        if form.is_valid():
            obj, created = my_restaurant_info_model.objects.get_or_create(user=request.user)
            name = form.cleaned_data["restaurant_name"]
            obj.restaurant_name = name
            obj.save(update_fields=["restaurant_name"] )
            pass
        pass
    else:
        form = restaurant_name_form()
        obj, created = my_restaurant_info_model.objects.get_or_create(user=request.user)
        print obj
        name = obj.restaurant_name
        print "xxxxxx",name, created
#product = Product.objects.get(name='Venezuelan Beaver Cheese')
#product.number_sold = 4
#product.save(update_fields=["active"] )
#
#        form = my_restaurant_info_form()
#        pass
    return render(request,'my_restaurant/my_restaurant_edit_info.html',{
        'name_form':form
    })
