from django.urls import path
from . import views
from .views import profile

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup'),
    path('movies/', views.movies, name='movies'),
    # path('movies/', views.get_movies, name='get_movies'), #i might change this 
    path('accounts/signup/',views.signup,name='signup'),
    path('profile/', profile, name='profile'),
]