from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# from django.http import HttpResponse
# Create your views here.


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {"rooms": rooms})


def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)
