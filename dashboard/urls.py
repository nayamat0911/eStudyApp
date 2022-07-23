
from django.urls import path

from .import views

app_name='dashboard_app'

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('notes/', views.Notes_page, name='notes'),
    path('delete-notes/<int:pk>', views.Delete_Note, name='deleted_note'),
    path('delete-details/<int:pk>', views.NotesDetailView.as_view(), name='note_details'),
    path('homework/', views.home_work, name='home_work'),
    path('update-homework/<int:pk>', views.update_homework, name='update_homework'),
]
    
