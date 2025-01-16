from django.urls import path
from . import views
from .views import profile

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup'),
    path('get_movie/<str:movie>/', views.get_movie, name='get_movies'), #i might change this 
    path('accounts/signup/',views.signup,name='signup'),
    path('profile/',views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update')
    
]