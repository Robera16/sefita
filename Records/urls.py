from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='records_index'),
    path('<int:record_id>', views.detail, name='records_detail')
]
