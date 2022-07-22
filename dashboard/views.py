from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def HomePage(request):
    return render(request,'dashboard/home.html')


def Notes(request):
    return render(request,'dashboard/notes.html')