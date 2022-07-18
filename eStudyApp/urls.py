from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dash/ ', include('dashboard.urls')),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
