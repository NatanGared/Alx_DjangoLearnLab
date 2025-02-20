from bookshelf.models import Book 

retrieved_book = Book.objects.get(title='1984')
print(retrieved_book)

#1984