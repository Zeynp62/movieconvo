from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup'),
    path('movies/', views.movies, name='movies'),
    path('get_movie/<str:movie_id>/', views.get_movies, name='get_movies'), #i might change this 
]