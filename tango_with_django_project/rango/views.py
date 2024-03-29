from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner! <br> <a href='/rango/about/'>About</a>")


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Valentin Dimitrov.'}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <br> <a href='/rango/'>Index</a>")

def ivailo_pavlov(request):
    context_dict = {'boldmessage': 'Trading page.'}
    return render(request, 'rango/trading.html', context=context_dict)