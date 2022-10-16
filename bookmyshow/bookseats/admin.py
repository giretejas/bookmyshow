from atexit import register
from django.contrib import admin
from .models import *


@admin.register(Movie)
class UserAdmin(admin.ModelAdmin):
    list_display=('Mid','movie_name','movie_duration','movie_rdate','movie_poster','movie_banner','movie_genre')
    
@admin.register(Shows)
class UserAdmin(admin.ModelAdmin):
    list_display=('shows','cinema','movie','time','date','price')


@admin.register(CinemaTheater)
class UserAdmin(admin.ModelAdmin):
    list_display=('cinema','role','cinema_name','phoneno','city')

admin.site.register(Bookings)