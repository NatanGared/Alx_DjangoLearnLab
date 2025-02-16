from bookshelf.models import Book

new_book.delete()

all_books = Book.objects.all()
print(all_books)

#<QuerySet []>
