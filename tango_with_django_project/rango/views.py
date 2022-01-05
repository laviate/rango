from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Rango says hey there partner! <br> <a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the about page. <br> <a href='/rango/'>Index</a>")


def ivailo_pavlov(request):
    return HttpResponse("Ивайло обича големи черни пишки<br>  "
                        "<img src='https://pasteimg.com/images/2022/01/04/ivailo.jpg' alt='Ivcho obicha patki'> ")
