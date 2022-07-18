from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def index(request):
    return render(request, 'dashboard/base.html') 

