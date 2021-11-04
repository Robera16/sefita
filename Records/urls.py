from django.contrib import admin
from django.conf import settings 
from django.urls import path
from django.conf.urls.static import static 

from . import views
urlpatterns = [
    path('', views.index, name='records_index'),
    path('<int:record_id>', views.detail, name='records_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
