from email import message
from multiprocessing import context
from pyexpat import model
from unittest import result
from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
from django.urls import is_valid_path



# for notes
from . models import Notes
from . forms import Notes, NoteForm
from django.views import generic

def HomePage(request):
    return render(request,'dashboard/home.html')


def Notes_page(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], description = request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} Successfully!")

    else:
        form  = NoteForm()

    notes_obj = Notes.objects.filter(user = request.user)
    context_note={
        'notes':notes_obj,
        'form':form,
    }
    return render(request,'dashboard/notes.html',context=context_note)

def Delete_Note(request, pk):
    Notes.objects.get(id=pk).delete()
    messages.warning(request,f" A Notes is deleted by '{request.user.username}'. ")
    return redirect("dashboard_app:notes")
    

class NotesDetailView(generic.DetailView):
    model = Notes
#   end Notes -------------------------------------

# HomeWork---------------------------------------------------------
# import Homework--------
from . models import HomeWork
from .forms import *

def home_work(request):
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished =False
            homeworks = HomeWork(
                user =  request.user,
                subject = request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished,
            )
            homeworks.save()
            messages.success(request, f"Homework Added from {request.user.username}!")
    else:    
        form = HomeWorkForm()
    homework = HomeWork.objects.filter(user = request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False

    home_context = {
        'homework':homework,
        'homework_done':homework_done,
        'form':form,

    }
    return render(request, 'dashboard/homework.html', context=home_context)

def update_homework(request, pk=None):
    homework = HomeWork.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished == False
    else:
        homework.is_finished == True
    homework.save(request.user)
    return redirect('dashboard_app:home_work')

def delete_homework(request, pk):
    HomeWork.objects.get(pk=pk).delete()
    messages.warning(request, f"A homework deleted by '{request.user.username}'.")
    return redirect('dashboard_app:home_work')

# end Homework---------------------------------------
#  You tube section start----===================================
from .forms import *
from youtubesearchpython import VideosSearch
def youtube(request):
    if request.method == "POST":
        form = DashBoardForm(request.POST)
        text = request.POST['text']
        video = VideosSearch(text,limit=10)
        result_list =[]
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnail':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'published':i['publishedTime'],
            }
            desc = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            context = {
                'form':form,
                'results': result_list,
            }
        return render(request, 'dashboard/youtube.html', context=context)
    else:
        form = DashBoardForm()

    context = {
        'form':form,
    }
    return render(request, 'dashboard/youtube.html', context=context)

# end youtube--------------------------------
# start TO DO===========================================================
from . forms import TodoForm
from . models import TODO

def To_Do(request):
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished =False
            todos = TODO(
                user = request.user,
                title = request.POST['title'],
                is_finished = finished
            )
            todos.save()
            messages.success(request, f"Todo added from {request.user.username}!!.")
    else:       
        form = TodoForm()
    todo = TODO.objects.filter(user = request.user)

    if len(todo) == 0:
        todos_done =True
    else:
        todos_done = False

    context = {
        'todos':todo,
        'form':form,
        'todos_done':todos_done
    }
    return render(request, 'dashboard/todo.html',context=context)