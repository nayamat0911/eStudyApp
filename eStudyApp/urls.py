from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

from dashboard import views as dash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', dash_views.register, name='register' )
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
