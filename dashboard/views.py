from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def HomePage(request):
    home_context={
        'title':'home',
        'text':"this is Home page"
    }
    return render(request,'dashbord/base.html', content=home_context)

