
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
    path('to-do/', views.To_Do, name='to_do'),
    



]

    
