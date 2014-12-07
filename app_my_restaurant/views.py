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
from django.db import connection

FOOD_PER_PAGE = 25

class my_restaurant_home(View):
    def get(self, request):
        if request.user.is_authenticated() is False:
            #return render(request, 'my_restaurant/my_restaurant_login.html')
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
def my_restaurant_up_desk(request,desk_id):
    return my_restaurant_desk(request)

@login_required
def my_restaurant_down_desk(request,desk_id):
    return my_restaurant_desk(request)

@login_required
def my_restaurant_remove_desk(request,desk_id):
    my_restaurant_desk_model.objects.filter(user=request.user,id=desk_id).delete()
    return my_restaurant_desk(request)

# only show edit info, when edit finish still call add_desk
@login_required
def my_restaurant_update_desk(request,desk_id):
    status = False
    if request.method == 'POST':
        pass
    else:
        pass
    try:
        edit_desk = my_restaurant_desk_model.objects.get(user=request.user, id=desk_id)
        form = restaurant_add_desk_form(initial={
            "desk_id":edit_desk.id,
            "desk_name":edit_desk.desk_name,
            "desk_person_count":edit_desk.desk_person_count,
            "desk_description":edit_desk.desk_description
        })
        pass
    except:
        print "update failed"
        pass
    return my_restaurant_desk(request, form, status)


@login_required
def my_restaurant_add_desk(request):
    # print request
    status = False
    if request.method == 'POST':
        form = restaurant_add_desk_form(request.POST)
        if form.is_valid():
            try:
                desk_id = form.cleaned_data["desk_id"]
                print "my dsk id",desk_id
                if desk_id>=0: # update desk
                    edit_desk = my_restaurant_desk_model.objects.get(user=request.user, id=desk_id)
                    edit_desk.desk_name = form.cleaned_data["desk_name"]
                    edit_desk.desk_person_count = form.cleaned_data["desk_person_count"]
                    edit_desk.desk_description = form.cleaned_data["desk_description"]
                    edit_desk.save()
                    status = True
                    pass
                else: # new desk
                    p = my_restaurant_desk_model.objects.create(user=request.user,
                                                                   desk_name = form.cleaned_data["desk_name"],
                                                                   desk_person_count = form.cleaned_data["desk_person_count"],
                                                                   desk_description = form.cleaned_data["desk_description"]
                                                                   )

                    status = True
                    pass
            except:
                status = False
                form._errors["desk_name"] = ErrorList([u"Error, the same desk already exist!"])
            pass
        else:
            status = False
            pass
    else:
        status = False
        form = restaurant_add_desk_form(initial={"desk_id":-1})
    # query string from django-table2 page switch
    if request.META['QUERY_STRING'].find("page")!=-1:
        status = True
        pass
    return my_restaurant_desk(request, form, status)

# desk edit home page
@login_required
def my_restaurant_desk(request,form=restaurant_add_desk_form(initial={"desk_id":-1}),return_status=True):
    # This enables data ordering and pagination.
    my_query = my_restaurant_desk_model.objects.filter(user=request.user)
    #print 'sql', my_query.query
    table = desk_table(my_query)
    RequestConfig(request, paginate={"per_page": FOOD_PER_PAGE}).configure(table)
    return render(request,
                  "my_restaurant/my_restaurant_edit_desk.html",
                  {
                      "desk_table": table,
                      "add_desk_form": form,
                      'return_status':return_status# default hide
                  })
