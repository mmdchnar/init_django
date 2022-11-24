from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.views.generic.base import RedirectView


def index(req):
    return render(req, 'index.html')
