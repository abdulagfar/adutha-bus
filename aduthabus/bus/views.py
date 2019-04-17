from django.shortcuts import render
from .models import bus_timetable
from collections import OrderedDict 
from django.http import Http404

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
  

def home_page(request,*args,**kargs):
    if request.method=='POST':
        source=request.POST.get("q_source")
        destination=request.POST.get("q_destination")
        return show_table(request,source,destination)
    context={}
    return render(request,"home.html",context)

def show_table(request,q_s,q_d,*args,**kargs):
    d=[]
  
    all_roots=bus_timetable.objects.all()

    
    for o in all_roots:
        got_s=False
        print(o.id)
        data = OrderedDict([ 
                                 (o.st_1, o.t_1), 
                                 (o.st_2, o.t_2),
                                 (o.st_3, o.t_3),
                                 (o.st_4, o.t_4),
                                 (o.st_5, o.t_5),
                                 (o.st_6, o.t_6),
                                ]) 
        
        for i ,t in data.items():
            # print(q_d)
            if str(i).lower()== str(q_s).lower():
                t_s=t
                got_s=True
                # print("in if one")
            if str(i).lower()== str(q_d).lower() and got_s==True:
                    context={
                        "b_id":o.id,
                        "b_name":o.bus_name,
                        "s_time":t_s,
                        "r_time":t
                        }
                    d.append(context)
                    got_s=False
                    break 


    d={"d":d,
    "s":q_s.upper(),
        "r":q_d.upper(),
    }

   
    
    return render(request,"show_table.html",d)
# Create your views here.

def bus_details(request,id,*args,**kargs):
    try:
        bus=bus_timetable.objects.get(id=id)
    except bus_timetable.DoesNotExist:
        raise Http404
    context={"bus":bus} 
    return render(request,"bus_details.html",context)

def redirect_to_login(request):
    return render(request, 'login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'add_data.html')
        else:
            return HttpResponse('Login Failed')
    else:
        return render(request, 'login.html')