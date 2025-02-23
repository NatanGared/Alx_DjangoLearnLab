from django.contrib import admin
from relationship_app.models import Library, Book, Author, Librarian

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)