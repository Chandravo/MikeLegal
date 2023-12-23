from django.shortcuts import render, redirect
from .models import *

import random
import string
# Create your views here.
def home(request, key):
    messages = Message.objects.filter(room__key=key).order_by('created_at')
    text = ""
    for message in messages:
        text+= "Anonymous: "+message.message+"\n"
        # print(message.message)
    return render(request, 'chatroom.html',{'key':key, 'text':text})

def createRoom(request):
    key = ''.join(random.choice(string.ascii_letters) for i in range(6))
    while (ChatRoom.objects.filter(key=key).exists()):
        key = ''.join(random.choice(string.ascii_letters) for i in range(6))
    room = ChatRoom.objects.create(key=key)
    room.save()
    return redirect('/info/'+key)

def joinRoom(request):
    key = request.POST['key']
    if (ChatRoom.objects.filter(key=key).exists()):
        return redirect('/info/'+key)
    else:
        return render(request, 'index.html', {'error':'Room does not exist'})

def index(request):
    
    return render(request, 'index.html', context = {'error':''})