from django.urls import path
from .views import list_books, LibraryDetailView, login, logout, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/',login, name='login'),
    path('logout/',logout, name='logout'),
    path('register/',register, name='register'),
]