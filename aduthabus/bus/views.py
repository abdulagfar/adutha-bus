from django.shortcuts import render
from .models import bus_timetable
from collections import OrderedDict
from django.http import Http404

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def home_page(request):

    if request.method == 'POST':

        source = request.POST.get("q_source")
        destination = request.POST.get("q_destination")

        if source == '' or destination == '':
            context = {'unavailable_msg': 'Enter source and destination.'}
            return render(request, "home.html", context)

        return show_table(request, source, destination)

    return render(request, "home.html")


def show_table(request, q_s, q_d, *args, **kargs):
    d = []

    all_roots = bus_timetable.objects.all()

    for o in all_roots:
        got_s = False

        data = OrderedDict([
            (o.st_1, o.t_1),
            (o.st_2, o.t_2),
            (o.st_3, o.t_3),
            (o.st_4, o.t_4),
            (o.st_5, o.t_5),
            (o.st_6, o.t_6),
        ])

        for i, t in data.items():

            if str(i).lower() == str(q_s).lower():
                t_s = t
                got_s = True

            if str(i).lower() == str(q_d).lower() and got_s:
                context = {
                    "b_id": o.id,
                    "b_name": o.bus_name,
                    "s_time": t_s,
                    "r_time": t
                }
                d.append(context)
                got_s = False
                break
    if d:
        d = {"d": d,
         "s": q_s.upper(),
         "r": q_d.upper(),
         }
        return render(request, "show_table.html", d)
    else:
        context = {'unavailable_msg': 'Invalid Source/Destination.'}
        return render(request, "home.html", context)



    
# Create your views here.


def bus_details(request, id, *args, **kargs):
    try:
        bus = bus_timetable.objects.get(id=id)
    except bus_timetable.DoesNotExist:
        raise Http404
    context = {"bus": bus}
    return render(request, "bus_details.html", context)


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
            return render(request, 'login.html',{"message": "Invalid UserName or Password"})
    else:
        return render(request, 'login.html')


@login_required
def add_data(request):
    context = {}
    if request.method == 'POST':
        bus_name = request.POST.get('bus_name')
        bus_number = request.POST.get('bus_number')

        station1 = request.POST.get('station1')
        time1 = request.POST.get('time1')
        station2 = request.POST.get('station2')
        time2 = request.POST.get('time2')
        station3 = request.POST.get('station3')
        time3 = request.POST.get('time3')
        station4 = request.POST.get('station4')
        time4 = request.POST.get('time4')
        station5 = request.POST.get('station5')
        time5 = request.POST.get('time5')
        station6 = request.POST.get('station6')
        time6 = request.POST.get('time6')

        data = bus_timetable(bus_name=bus_name, bus_no=bus_number, st_1=station1,
                             t_1=time1, st_2=station2, t_2=time2, st_3=station3, t_3=time3, st_4=station4, t_4=time4, st_5=station5, t_5=time5, st_6=station6, t_6=time6)
        data.save()

        context['success_message'] = 'Data Added'
        return render(request, 'add_data.html', context)

    return render(request, 'add_data.html', context)


@login_required
def admin_logout(request):
    logout(request)
    return render(request, 'login.html')
