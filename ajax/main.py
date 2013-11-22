#encoding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import sys
sys.path.insert(0, '../')
reload(sys)
sys.setdefaultencoding('utf-8')
from echarts.line import Line
from echarts.pie import Pie
from echarts.map import Map


def line(request):
    r = request.GET
    id, type, data = r['id'], r['type'], r['data']

    l = Line(
        id = id,
        type = type,
        data = data,
    )
   
    return HttpResponse('%s({"js":"%s"})' % (request.GET['callback'], l.create()   ))


def pie(request):
    r = request.GET
    id, type, data = r['id'], r['type'], r['data']

    p = Pie(
        id = id,
        type = type,
        data =data,
    )

    return HttpResponse('%s({"js":"%s"})' % (request.GET['callback'], p.create()   ))


def map(request):
    r = request.GET
    id, type, data = r['id'], r['type'], r['data']

    m = Map(
        id = id,
        type = type,
        data =data,
    )

    return HttpResponse('%s({"js":"%s"})' % (request.GET['callback'], m.create()   ))






