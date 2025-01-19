from django.urls import path
from . import views
from .views import profile

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('accounts/signup/',views.signup,name='signup'),
    path('movies/', views.movies, name='movies'),
    # path('movies/', views.get_movies, name='get_movies'), #i might change this 
    path('profile/', profile, name='profile'),
    path('profile/<int:user_id>/update/', views.ProfileUpdate.as_view(), name='profile_update'), 
    path('profile/<int:user_id>/',views.ProfileDetail.as_view(), name='profile_detail'),
    path('add_to_watchlist/<int:movie_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist_detail, name='watchlist_detail'),
]