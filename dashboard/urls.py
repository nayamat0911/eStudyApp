
from django.urls import path

from .import views

app_name='dashboard_app'

urlpatterns = [
    path('', views.HomePage, name='home'),
    #notes--------
    path('notes/', views.Notes_page, name='notes'),
    path('delete-notes/<int:pk>', views.Delete_Note, name='deleted_note'),
    path('delete-details/<int:pk>', views.NotesDetailView.as_view(), name='note_details'),
    #homework----------
    path('homework/', views.home_work, name='home_work'),
    path('update-homework/<int:pk>', views.update_homework, name='update_homework'),
    path('delete-homework/<int:pk>', views.delete_homework, name='delete_homework'),
    #youtube-----------
    path('youtube/', views.youtube, name='youtube'),

    #to-do-----------
    path('todo/', views.To_Do, name='to_do'),
    path('update-todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete_todo'),
    
    # books-----------
    path('books/', views.books, name='books'),

    # dictionary -------
    path('dictionary/', views.dictionary, name='dictionary'),

    # wiki ----------------
    path('wiki/', views.wiki, name = 'wiki'),

    #conversion---------
    path('conversion/', views.conversion, name = 'conversion')



]

    
