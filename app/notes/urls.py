from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]
