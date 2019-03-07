from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    context = {
        'info': ['username', 'email', 'pin', 'alias', 'website', 'address']
     }
    return HttpResponse(render(request, 'profiles/new.html', context))
