from django.urls import path
from . import views

urlpatterns = [
    path('movie/',views.movie_list,name='movie_list'),
    path('movie/forms',views.movie_form,name='movie_form')
]