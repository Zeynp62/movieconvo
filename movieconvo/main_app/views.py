from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile



class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = ['avatar', 'bio']
    def form_valid (self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    



# Create your views here.

@login_required
def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def get_movie(request, movie):
    url = f'https://api.themoviedb.org/3/movie/{movie}?api_key=API_KEY'
    response = request.get(url)
    data = response.json()
    return JsonResponse(data)


def signup(request):
    error_message=''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)#to login the user directly after signing up
            return redirect('index')
        else:
            error_message='Invalid Sign-up please try again later.'
    form = UserCreationForm()
    context={'form':form,'error_message':error_message}
    return render(request,'registration/signup.html',context)