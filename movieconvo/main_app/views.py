from .models import Movie, Genre
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.http import JsonResponse
from django.urls import reverse
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


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['avatar', 'bio']
    def form_valid (self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    

    
class ProfileUpdate(LoginRequiredMixin, UpdateView,):
    model = Profile
    fields = ['avatar', 'bio']
    

    def get_object(self):
        # Fetch the Profile object for the user
        return Profile.objects.get(user__id=self.kwargs['user_id'])
    
    
    def get_success_url(self):
        return reverse('profile_detail', kwargs={'user_id': self.object.user.id})


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile

    def get_object(self):
        return Profile.objects.get(user__id=self.kwargs['user_id'])

@login_required
def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

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
    Movie.objects.bulk_create(api_data_objects)

    return render(request, 'all_movies.html', {'display_movie':display_movie})
    
    #  def form_valid(self, form):
    #     form.instance.user= self.request.user
    #     return super().form_valid(form)




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
            return redirect('profile_update', user_id=user.id)
        
        else:
            error_message='Invalid Sign-up please try again later'
        
        success_url = '/profile/<int:pk>/update/'
    form = UserCreationForm()
    context={'form':form,'error_message':error_message}
    return render(request,'registration/signup.html',context)