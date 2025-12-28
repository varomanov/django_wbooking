from django.shortcuts import render, redirect
from .models import Person, Place, Booking
from datetime import date

menus = [
    {'name': 'Бронь', 'path': 'booking'},
    {'name': 'Журнал', 'path': 'journal'},
    {'name': 'Этажи', 'path': 'floor'},
    {'name': 'КИР', 'path': 'kir'},
]

def booking(request):
    places = Place.objects.all()
    persons = Person.objects.all()
    if request.method == 'POST':
        person_id = request.POST.get('person')
        place_id = request.POST.get('place')
        try:
            Booking.objects.create(
                person=Person.objects.get(id=person_id), 
                place=Place.objects.get(id=place_id),
                booked_date=date.today()
            )
            return redirect('journal')
        except:
            return redirect('booking')
    
    context = {
        'pagename': 'Бронирование',
        'menus': menus,
        'selected': 'booking',
        'places': places,
        'persons': persons
    }
    return render(request, 'pages/booking.html', context)


def journal(request):
    bookings = Booking.objects.all()
    context = {
        'pagename': 'Журнал',
        'menus': menus,
        'selected': 'journal',
        'bookings': bookings
    }
    return render(request, 'pages/journal.html', context)


def floor(request):
    context = {
        'pagename': 'Этажи',
        'menus': menus,
        'selected': 'floor'
    }
    return render(request, 'pages/floor.html', context)


def kir(request):
    context = {
        'pagename': 'КИР',
        'menus': menus,
        'selected': 'kir'
    }
    return render(request, 'pages/kir.html', context)