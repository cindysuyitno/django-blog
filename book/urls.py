from django.urls import path
from . import views

urlpatterns=[
    path('book/',views.book_list,name='book_list'),
    path('book/author/<int:pk>/',views.author_detail,name='author_detail'),
    path('book/post_form/',views.post_form,name='post_form'),
    path('book/book_detail/<int:pk>/',views.book_detail,name='book_detail')
]