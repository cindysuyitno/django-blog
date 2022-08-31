from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PostForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books':books})

def author_detail(request,pk):
    author_detail = get_object_or_404(AuthorDetail,pk=pk)
    book = Book.objects.filter(author=author_detail.author)
    return render(request, 'book/author_detail.html', {'author':author_detail,'book':book})

def post_form(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('book_list')
    else: form = PostForm()
    return render(request, 'book/post_form.html', {'form':form})

def book_detail(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'book/book_detail.html', {'book':book})