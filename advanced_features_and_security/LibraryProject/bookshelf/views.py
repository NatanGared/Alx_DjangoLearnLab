from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Library
from .forms import ExampleForm

@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list view
    return render(request, 'bookshelf/delete_book.html', {'book': book})

@permission_required('bookshelf.can_view_library', raise_exception=True)
def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'bookshelf/library_list.html', {'libraries': libraries})
