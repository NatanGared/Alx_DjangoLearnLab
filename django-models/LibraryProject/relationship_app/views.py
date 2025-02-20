# relationship_app/views.py

from django.shortcuts import render
from bookshelf.models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic import DetailView
from bookshelf.models import Book 

class LibraryDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html' 

    def get_queryset(self):
        library_id = self.kwargs['name']
        return Book.objects.filter(library__id=library_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library_name'] = "Library Name" 
        return context