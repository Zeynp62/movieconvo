from .models import Movie, Genre
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os 
from dotenv import load_dotenv
load_dotenv()

KEY=os.getenv('API_KEY')

GENRE_MAPPING = {
    28: 'Action',
    12: 'Adventure',
    16: 'Animation',
    35: 'Comedy',
    80: 'Crime',
    99: 'Documentary',
    18: 'Drama',
    10751: 'Family',
    14: 'Fantasy',
    36: 'History',
    27: 'Horror',
    10402: 'Music',
    9648: 'Mystery',
    10749: 'Romance',
    878: 'Science Fiction',
    10770: 'TV Movie',
    53: 'Thriller',
    10752: 'War',
    37: 'Western'
}

# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

#get all the movies from the database and display them
def movies(request):
    display_movie= Movie.objects.all()
    

    url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={KEY}'
    response = requests.get(url)
    data = response.json()

  
    
    api_data_objects = [
        Movie(
            title=item.get('title'),
            # genre=item.get('genre_ids',[]),
            rating=item.get('adult'),
            description=item.get('overview'),
            poster=item.get('poster_path'),
            trailer=item.get('video'),
        )
        for item in data['results']
    ]
    print("hi",api_data_objects)
    Movie.objects.bulk_create(api_data_objects)

    return render(request, 'all_movies.html', {'display_movie':display_movie})
    
    #  def form_valid(self, form):
    #     form.instance.user= self.request.user
    #     return super().form_valid(form)



# #to get the movies from the api and adds to the database....
# def get_movies(requests):
#     url = f'https://api.themoviedb.org/3/trending/movie/day?api_key={KEY}'
#     response = requests.get(url)
#     data = response.json()
    
#     api_data_objects = [
#         Movie(
#             title=item.get('title'),
#             genre=item.get('genre_ids',[]),
#             rating=item.get('adult'),
#             description=item.get('overview'),
#             poster=item.get('poster_path'),
#             trailer=item.get('video'),
#         )
#         for item in data['results']
#     ]
#     print("hi",api_data_objects)
#     Movie.objects.bulk_create(api_data_objects)



    # title=data.get('title')
    # description=data.get('overview')
    # year=data.get('release_date')
    # poster = data.get('poster_path')
    # trailer = ""
    # if 'videos' in data and len(data['videos']['results']) > 0:
    #     trailer = f"https://www.youtube.com/embed/{data['videos']['results'][0]['key']}"
    # rating = 'N'  
    # if 'adult' in data:
    #     rating = 'R' if data['adult'] else 'PG' 
    
    # movie = Movie.objects.update_or_create(title=title, defaults={
    #     'description': description,
    #     'year': year,
    #     'poster': poster,
    #     'trailer': trailer,
    #     'rating': rating,
    # })

# genre_ids = data.get('genre_ids',[])
# genre_objects = []

# for genre_id in genre_ids:
#     genre_name = GENRE_MAPPING(genre_id)
#     if genre_name:
#             genre_obj = Genre.objects.get_or_create(name=genre_name)
#             genre_objects.append(genre_obj)

#     movie.genre.set(genre_objects)

    # return JsonResponse(data)

def signup(request):
    error_message=''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)#to login the user directly after signing up
            return redirect('index')
        else:
            error_message='Invalid Sign-up please try again later'
    form = UserCreationForm()
    context={'form':form,'error_message':error_message}
    return render(request,'registration/signup.html',context)