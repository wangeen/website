# Create your views here.
# Create your views here.
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app_my_restaurant.models import my_restaurant_info_model
from app_my_restaurant.models import my_restaurant_desk_model
from app_my_restaurant.forms import restaurant_name_form
from app_my_restaurant.forms import restaurant_add_desk_form
from django_tables2   import RequestConfig
from app_my_restaurant.tables import desk_table
from django.forms.util import ErrorList

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
    obj, created = my_restaurant_info_model.objects.get_or_create(user=request.user)
    form = restaurant_name_form(initial={'restaurant_name': obj.restaurant_name,
                                         'restaurant_description': obj.restaurant_description
                                         })
    return render(request,'my_restaurant/my_restaurant_edit_info.html',{
        'name_form':form
    })

@login_required
def my_restaurant_menu(request):
    return render_to_response('my_restaurant/my_restaurant_edit_menu.html',  context_instance=RequestContext(request))

@login_required
def my_restaurant_update_name(request):
    if request.method == 'POST':
        form = restaurant_name_form(request.POST)
        print request.user
        if form.is_valid():
            obj, created = my_restaurant_info_model.objects.get_or_create(user=request.user)
            obj.restaurant_name = form.cleaned_data["restaurant_name"]
            obj.restaurant_description = form.cleaned_data["restaurant_description"]
            #obj.save(update_fields=["restaurant_name"] )
            obj.save()
            pass
        pass
    else:
        form = restaurant_name_form()
    return render(request,'my_restaurant/my_restaurant_edit_info.html',{
        'name_form':form,
        'save_success':True
    })

@login_required
def my_restaurant_remove_desk(request):
    if request.method == 'POST':
        pass
    else:
        pass
    # This enables data ordering and pagination.
    table = desk_table(my_restaurant_desk_model.objects.all())
    RequestConfig(request, paginate={"per_page": 5} ).configure(table)
    return render(request,'my_restaurant/my_restaurant_edit_desk.html',{
        'add_desk_form':form,
        "desk_table": table,
        'return_status':status
    })




@login_required
def my_restaurant_add_desk(request):
    status = False
    if request.method == 'POST':
        form = restaurant_add_desk_form(request.POST)
        print request.user
        if form.is_valid():
            try:
                p = my_restaurant_desk_model.objects.create(user=request.user,
                                                                   desk_name = form.cleaned_data["desk_name"],
                                                                   desk_person_count = form.cleaned_data["desk_person_count"],
                                                                   desk_description = form.cleaned_data["desk_description"]
                                                                   )
                status = True
            except:
                status = False
                form._errors["desk_name"] = ErrorList([u"Error, the same desk already exist!"])
            pass
        else:
            status = False
            pass
    else:
        status = False
        form = restaurant_add_desk_form()
    # This enables data ordering and pagination.
    table = desk_table(my_restaurant_desk_model.objects.all())
    RequestConfig(request, paginate={"per_page": 5} ).configure(table)
    return render(request,'my_restaurant/my_restaurant_edit_desk.html',{
        'add_desk_form':form,
        "desk_table": table,
        'return_status':status
    })



# desk edit home page
@login_required
def my_restaurant_desk(request):
    form = restaurant_add_desk_form()
    # This enables data ordering and pagination.
    table = desk_table(my_restaurant_desk_model.objects.all())
    RequestConfig(request, paginate={"per_page": 5}).configure(table)
    return render(request,
                  "my_restaurant/my_restaurant_edit_desk.html",
                  {
                      "desk_table": table,
                      "add_desk_form": form,
                      'return_status':True # default hide
                  })
