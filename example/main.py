from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def line(request):
    return render_to_response("example/line.html") 

def pie(request):
    return render_to_response("example/pie.html") 

def map(request):
    return render_to_response("example/map.html") 

def test(request):
    return render_to_response("example/test.html") 
