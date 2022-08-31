from django.contrib import admin
from .models import Author, AuthorDetail, Book, Publisher

admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
admin.site.register(Publisher)
