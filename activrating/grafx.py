# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Activity_rating_site.settings')
django.setup()

import matplotlib as mpl
import matplotlib.pyplot as plt

from activrating.models import Activities
import datetime


def duration(td):

    m, s = divmod(td, 60)
    m = (m/60)
    return  m

def plotl(day, r):
    title = ['Растояние км.', "Растояние км.", "Время"]
    title2 = ['Растояние', "Растояние", "Время"]
    colr = ['#5dbecd', '#feb67c', '#f5d657']
    r=r
    days = day
    rec = recordstat(days)



    mpl.rcParams['ytick.labelsize']='x-large'
    mpl.rcParams['xtick.labelsize'] = 'x-large'
    for i in range(len(rec)):
        fig = plt.figure()

        rundata = rec[i][0]
        runname = rec[i][1]
        plt.bar(runname, rundata, width = 0.4, color = colr[i])
        plt.title(title[i], fontsize=16 )
        plt.ylabel(title2[i],  fontsize=16)

        plt.grid(False)

        fig.savefig('./static/activrating/images/barshoris'+r[i]+'.png')



def recordstat(days):
    if  not days:
        sevendays = datetime.timedelta(days=30)

    else:

        sevendays = datetime.timedelta(days = days)
    week = datetime.date.today()-sevendays
    actw = Activities.objects.filter(startTimeLocal__gte=week)

    names = []
    for nam in actw:
        names.append(nam.ownerFullName)

    names = list(set(names))

    reclist = [[[],[]],[[],[]],[[],[]]]

    for nam in names:
        bc, hc, rc = 0, 0, 0
        ava= ''

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

            if  act.ownerFullName == nam:

                hc += float(act.duration)

        rc = int(rc)/1000
        bc = int(bc)/1000
        hc = duration(hc)

        reclist[0][0].append(rc)
        reclist[0][1].append(nam)
        reclist[1][0].append(bc)
        reclist[1][1].append(nam)
        reclist[2][0].append(hc)
        reclist[2][1].append(nam)

    return reclist

def weekmons():
    days = [6, 29]
    r =[['run', 'bike', 'hard'], ['run1', 'bike1', 'hard1']]
    for i in range(len(days)):
        day = days[i]
        plotl(day, r[i])


if __name__ == '__main__':
    weekmons()


