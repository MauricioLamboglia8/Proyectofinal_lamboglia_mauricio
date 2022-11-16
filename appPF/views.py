from django.shortcuts import render
from django.template import loader, context


def inicio(request):
    return render(request, "appPF/base.html")
   