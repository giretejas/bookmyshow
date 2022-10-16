from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Movie(models.Model):
    Mid = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=50)
    movie_duration = models.CharField(max_length = 300,default="2hr 45m")
    movie_rdate = models.CharField(max_length=50 ,default = "null")
    movie_poster = models.ImageField(default = "media/MovieCardPosters/boys3.jpg")
    movie_banner = models.ImageField(default = "media/MovieCardPosters/Shivpratap.jpg")
    movie_genre = models.CharField(max_length = 50,default="Action | Historical ")

    def __str__(self):
        return self.movie_name

class CinemaTheater(models.Model):
    cinema=models.AutoField(primary_key=True)
    role=models.CharField(max_length=30,default='cinema_manager')
    cinema_name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=15)
    city=models.CharField(max_length=100)
    

    def __str__(self):
        return self.cinema_name
    
class Shows(models.Model):
    shows=models.AutoField(primary_key=True)
    cinema=models.ForeignKey(CinemaTheater,on_delete=models.CASCADE, related_name='cinema_show')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='movie_show')
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=15, default="")
    price=models.IntegerField()

    def __str__(self):
        return self.cinema.cinema_name +" | "+ self.movie.movie_name +" | "+ self.time



class Bookings(models.Model):
    shows = models.ForeignKey(Shows, on_delete=models.CASCADE)
    useat = models.CharField(max_length=100)
    
    @property
    def useat_as_list(self):
        return self.useat.split(',')
    def __str__(self):
        return self.shows.movie.movie_name +" | "+ self.useat
