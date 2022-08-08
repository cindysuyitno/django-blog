from django.shortcuts import render, redirect
from .models import Movie, Actor
from .forms import MovieForm

def movie_list(request):
    movie = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movie':movie})

def movie_form(request):
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form':form})
