from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Users, Activities
import datetime
import activrating.grafx


def runusers(request):
    f = Activities.objects.order_by('-startTimeLocal')[:10]
    context = {'userActivities': f}
    return render(request, "activrating/index.html", context)


def userform(request,activityId):
    f = Activities.objects.get(activityId=activityId)
    act = Activities.objects.filter(ownerId = f.ownerId).order_by("-startTimeLocal")[:7]
    context = {'userActivities': f, 'act':act}
    return render(request, "activrating/userprofile.html", context)


def recordstat(request,days=6):

    if  days == 6:
        sevendays = datetime.timedelta(days=6)
        rgafdays = ['activrating/images/barshorisrun.png', 'activrating/images/barshorisbike.png', 'activrating/images/barshorishard.png']
    else:
        sevendays = datetime.timedelta(days=days)
        rgafdays = ['activrating/images/barshorisrun1.png', 'activrating/images/barshorisbike1.png', 'activrating/images/barshorishard1.png']
    week = datetime.date.today()-sevendays
    actw = Activities.objects.filter(startTimeLocal__gte=week)
    names = []
    for nam in actw:
        names.append(nam.ownerFullName)
    names = list(set(names))
    runlist, bikelist, hardlist= [],[],[]
    for nam in names:
        bc, hc, rc = 0, 0, 0
        ava= ''
        tup1 = ()
        tup2 = ()
        tup3 = ()

        for act in actw:
            if act.ownerFullName == nam and act.activityType == '1' or act.activityType == '18' or act.activityType == '11' or act.activityType == '9':
                rc += float(act.distance)
            if act.ownerFullName == nam:
                ava = act.ownerProfileImageUrlMedium
            if act.activityType == '2' and act.ownerFullName == nam:
                if act.distance == None:
                    bc = 0
                else:
                    bc += float(act.distance)
            if act.ownerFullName == nam:
                hc += float(act.duration)
            else:
                continue

        tup1 = (rc, nam, ava)
        tup2 = (bc, nam, ava)
        tup3 = (hc, nam, ava)
        runlist.append(tup1)
        bikelist.append(tup2)
        hardlist.append(tup3)
    runlist.sort(reverse=True)
    bikelist.sort(reverse=True)
    hardlist.sort(reverse=True)

    context = {'rlist': runlist, 'blist': bikelist, 'hlist': hardlist, 'graf': rgafdays}
    return render(request, "activrating/record.html", context)


def userlist(request):
    u_list = Activities.objects.order_by('ownerId').distinct('ownerId')
    context = {'uslist': u_list}
    return render(request, 'activrating/userslist.html', context)


def homepage(request):
    return render(request, 'activrating/home.html')








