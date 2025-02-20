from relationship_app.models import Author
from relationship_app.models import Library
from relationship_app.models import Library

author = Author.objects.get(name='Author Name')
books_by_author = author.books.all()  

for book in books_by_author:
    print(book.title)

library = Library.objects.get(name='library_name') 
books_in_library = library.books.all() 

for book in books_in_library:
    print(book.title)

library = Library.objects.get(name='library_name') 
librarian = library.librarian 

if librarian:
    print(librarian.name)
else:
    print("No librarian assigned to this library.")