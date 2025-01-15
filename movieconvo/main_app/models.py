from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATINGS = (
    ('N', 'Not Rated'),
    ('PG', 'Parental Guide'),
    ('PG13','Parental Guide-13'),
    ('R', 'Rated R')
)

# Create your models here.
class Genre(models.Model):
    gid=models.IntegerField(max_length=60)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genres_detail',kwargs={'pk': self.id})

class Movie(models.Model):
    title = models.CharField(max_length=180)
    genre=models.ManyToManyField(Genre)
    rating= models.CharField(max_length=5,choices=RATINGS, default=RATINGS [0][0])
    description=models.TextField(max_length=1000)
    year = models.PositiveIntegerField()
    poster = models.URLField(default='images/default.jpg')
    trailer = models.URLField(blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})
    
    
class Watchlist(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('watchlists_detail', kwargs={'watchlist_id': self.id})

class Review(models.Model):
    movie=models.ForeignKey(Genre, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'reviews_id': self.id})
    review=models.TextField(max_length=500)






