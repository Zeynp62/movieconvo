from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup')
    path('get_movie/<str:movie>/', views.get_movie, name='get_movies'), #i might change this 
]