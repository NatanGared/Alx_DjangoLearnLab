# relationship_app/views.py

from django.shortcuts import render, redirect
from bookshelf.models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import View

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'
    success_url = reverse_lazy('relationship/list_books')  


class LogoutView(LogoutView):
    next_page = reverse_lazy('logout')


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
        return render(request, 'relationship_app/register.html', {'form': form})
