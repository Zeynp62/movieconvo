from django.urls import path
from . import views
from .views import profile

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup'),
<<<<<<< HEAD
    path('movies/', views.movies, name='movies'),
    path('get_movie/<str:movie_id>/', views.get_movies, name='get_movies'), #i might change this 
=======
    path('get_movie/<str:movie>/', views.get_movie, name='get_movies'), #i might change this 
    path('accounts/signup/',views.signup,name='signup'),
    path('profile/', profile, name='profile'),
    
>>>>>>> 37d605edcaa362ec7e17801a8cc39743610efe26
]