from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader
import os

def finish(path):
    if os.path.isfile(path + "fin.log"):
        return True
    return False

def render_report(request, sha):
    path = "/home/zozanh/env/djcode/thesis/static/data/"
    if sha:
        if finish(path + sha + '/'):
                c = RequestContext(request, {'sha': sha+'/'})
                return render_to_response('report.html', c)
        else:
            c = RequestContext(request, {'sha': ""})
            return HttpResponseRedirect("/")
    else:
        c = RequestContext(request, {'sha': ""})
        return render_to_response('report.html', c)
