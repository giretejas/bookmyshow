from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    return render(request,'index.html',{'movie':movie})

def movie(request, id):
    movies = Movie.objects.get(Mid=id)
    cin = CinemaTheater.objects.filter(cinema_show__movie=movies).prefetch_related('cinema_show').distinct()  # get all cinema Thearers
    show = Shows.objects.filter(movie=id)
    context = {
        'movies':movies,
        'show':show,
        'cin':cin,
    }
    return render(request, "movie.html", context )

def seat(request, id):
    show = Shows.objects.get(shows=id)
    seat = Bookings.objects.filter(shows=id)
    return render(request,"seat.html", {'show':show, 'seat':seat})    



def booked(request):
    if request.method == 'POST':
        seat = ','.join(request.POST.getlist('check'))
        show = request.POST['show']
        book = Bookings(useat=seat, shows_id=show)
        book.save()
        return render(request,"booked.html", {'book':book})    
        

def ticket(request, id):
    ticket = Bookings.objects.get(id=id)
    print(ticket.shows.price)
    return render(request,"ticket.html", {'ticket':ticket})
