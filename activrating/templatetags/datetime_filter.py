# -*- coding: utf-8 -*-
"""Application filter for `datetime`_ 24 hours.

.. _datetime: https://docs.python.org/2/library/datetime.html
"""
import os, sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Activity_rating_site.settings')
django.setup()

from django import template
from datetime import date, timedelta

register = template.Library()


@register.filter(name='format_datetime')
def duration(td):
    if not td:
        return '0'
    else:
        td = int(float(td))

    m, s = divmod(td, 60)
    h, m = divmod(m, 60)
    if h == 0:
        return "%02d:%02d" % (m, s)
    else:
        return "%d:%02d:%02d" % (h, m, s)


@register.filter(name='format_distance')
def distance(dist):
    if dist == None:
        return '0'
    dist = int(float(dist))
    km = dist/1000
    m = format(km, '.2f')
    return "%s км" % ( m)


@register.filter(name = 'speed_Kmh')
def speedkmh(avs):
    if avs == None:
        return '0'
    avs = float(avs)
    kh = int(avs*3.6)
    return "%s км/ч" %(kh)


@register.filter(name = 'temp_average')
def tempaverage(avs):
    if avs == None:
        return '0'
    avs = float(avs)
    if avs == 0.0:
        return "%s" % (0)
    else:
        temp = 50/(avs*3)
        temp = format(temp, ".2f")
        return "%s мин/км" % (temp )


@register.filter(name = 'averHR')
def averHR(ahr):
    if ahr == None:
        return '0'
    ahr= int(float(ahr))
    return '%s уд/мин' %(ahr)


@register.filter(name = 'temp_average2')
def tempaverage2(avs):
    avs = float(avs)
    if avs == 0.0:
        return "%s" % (0)
    else:
        temp = 50/(avs*3)
        temp = format(temp, ".2f")
        return "%s м/км" % (temp)


@register.filter(name = 'elevation')
def elevationS(elev):
    if elev == None:
        return '0'
    elev = round(float(elev))
    return '%s м' % (elev)


@register.filter(name= 'cadens')
def avrcadens(cad):
    if cad == None:
        return '0'
    else:
     cad = int(float(cad))
     return '%s' % (cad)


@register.filter(name='averHR2')
def averHR2(ahr):
    if ahr == None:
        return '0'
    ahr = int(float(ahr))
    return '%s' % (ahr)


@register.filter(name= 'bikecadens')
def avrcadens(cad):
    if cad == None:
        return '0'
    else:
     cad = int(float(cad))
     return '%s об/мин' % (cad)


@register.filter(name = 'hrvprocent')
def hrvprocent(ahr):
    if not ahr:
        return "%s" %(0)
    else:
        proc = 180/100
        proc1 = int(float(ahr)/proc)
        return '%s' % (proc1)
