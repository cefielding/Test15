from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):

    dest1 = Destination()
    dest1.name = 'Orange'
    dest1.desc = 'Tasty citrus round fruit which is orange'
    dest1.img = 'card-item-1.png'
    dest1.price = 700 
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Grapes'
    dest2.desc = 'Small purple or green juicy fruits'
    dest2.img = 'card-item-2.png'
    dest2.price = 200
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Gauva'
    dest3.desc = 'Exotic fruit spelt weirdly'
    dest3.img = 'card-item-3.png'
    dest3.price = 400
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request,'index.html', {'dests': dests})
