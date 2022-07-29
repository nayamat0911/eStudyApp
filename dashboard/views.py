from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect




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

# update to do--------------

def update_todo(request, pk):
    todo = TODO.objects.get(pk=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('dashboard_app:to_do')  

def delete_todo(request, pk):
    TODO.objects.get(pk=pk).delete()
    return redirect('dashboard_app:to_do')
# end todo-------------------------------------

# start books session =============================================
import requests


def books(request):
    if request.method == "POST":
        form = DashBoardForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json() 
        result_list =[]
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
                
            }
            
            result_list.append(result_dict)
            context = {
                'form':form,
                'results': result_list,
            }
        return render(request, 'dashboard/books.html', context=context)
    else:
        form = DashBoardForm()

    context = {
        'form':form,
    }
    return render(request, 'dashboard/books.html',context=context)

# end books session-----------------

# start Dictionary =================================================

def dictionary(request):
    if request.method == "POST":
        form = DashBoardForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text
        r = requests.get(url)
        answer = r.json() 
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitins'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions']['synonyms']
            context_dic = {
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms,
            }
        except:
            context_dic={
                'form':form,
                'input':''
                }
        return render(request,'dashboard/dictionary.html',context=context_dic)
    else:
        form = DashBoardForm()
    context_dic = {
        'form':form,

    }
    return render(request, 'dashboard/dictionary.html',context=context_dic)

# end dictionary -------------------------------------
# start wiki =======================================================
import wikipedia

def wiki(request):
    if request.method == "POSt":
        text = request.POST['text']
        form = DashBoardForm(request.POST)
        search = wikipedia.page(text)
        context={
            'form':form,
            'title':search.title,
            'link':search.url,
            'details':search.summary,

        }
        return render(request, 'dashboard/wiki.html',context)
    else:
        form = DashBoardForm()
        context={
            'form':form,
        }
    return render(request, 'dashboard/wiki.html',context)

# conversion ===========================================================
def conversion(request):
    if request.method =="POST":
        form = ConversionForm(request.POST)
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard = {int(input)*3} foot'

                    if first == 'foot' and second == 'yard':
                        answer = f'{input} foot = {int(input)/3} yard'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }
        if request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            context = {
                'form':form,
                'm_form':measurement_form,
                'input':True
            }
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >=0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound = {int(input)*0.453592} kilogram'

                    if first == 'kilogram' and second == 'pound':
                        answer = f'{input} kilogram = {int(input)*2.20462} pound'
                context = {
                    'form':form,
                    'm_form':measurement_form,
                    'input':True,
                    'answer':answer
                }
    else:
        form = ConversionForm()
    context={
        'form':form,
        'input':False,

    }
    return render(request, 'dashboard/conversion.html',context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created for {username} !!")
    else:
        form = UserRegistationForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/register.html', context)



