from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# RATINGS = (
#     ('N', 'Not Rated'),
#     ('PG', 'Parental Guide'),
#     ('R', 'Rated R')
# )

# Create your models here.
class Genre(models.Model):
    gid=models.IntegerField()
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genres_detail',kwargs={'pk': self.id})

class Movie(models.Model):
    m_id = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=180)
    genre=ArrayField(models.CharField(max_length=50), size=5, default=list, blank=True, null=True)
    adult=models.BooleanField(default=False)
    # rating= models.CharField(max_length=5,choices=RATINGS, default=RATINGS [0][0])
    description=models.TextField(max_length=1000)
    year = models.CharField(max_length=10)
    poster = models.URLField(default='images/default.jpg')
    votes=models.FloatField(default=0.0)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})
    
    
class Watchlist(models.Model):
    movie=models.ManyToManyField(Movie, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('watchlists_detail', kwargs={'watchlist_id': self.id})


class Review(models.Model):
    movie=models.ForeignKey(Genre, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'reviews_id': self.id})
    review=models.TextField(max_length=500)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='', upload_to='main_app/static/profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
