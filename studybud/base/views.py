from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message
from .forms import RoomForm

# from django.http import HttpResponse
# Create your views here.


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist')

    page = 'login'
    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def registerPage(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


# update user with profile pic
# al topics page
# count with list
# activity separate page


def userProfile(request, id):
    user = User.objects.get(id=id)
    rooms = user.room_set.all()
    topics = Topic.objects.all()
    room_message = user.message_set.all()
    context = {'user': user, 'rooms': rooms, 'room_message': room_message, 'topics': topics}
    return render(request, 'base/profile.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms_query = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))

    # for paginations
    page = request.GET.get('page') if request.GET.get('page') != None else 1
    limit = request.GET.get('limit') if request.GET.get('limit') != None else 5
    rooms_paginate = Paginator(rooms_query, limit)
    rooms = rooms_paginate.get_page(page)

    topics = Topic.objects.all()
    rooms_count = rooms_query.count()

    room_message = Message.objects.filter(Q(room__topic__name__icontains=q))
    return render(request, 'base/home.html', {"rooms": rooms, "room_paginate": rooms_paginate, "topics": topics, "rooms_count": rooms_count, "room_message": room_message})


def room(request, id):
    room = Room.objects.get(id=id)
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()

    # message box
    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', id=room.id)

    context = {'room': room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)


# previous list or cerate topic fix
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here!!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteMessage(request, id):
    message = Message.objects.get(id=id)

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})
