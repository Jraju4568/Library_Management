from django.urls import path

from . import views

urlpatterns = [
    path('student_books/', views.allbooks, name='all_books'),
]