from django.shortcuts import render
from .models import *
# Create your views here.
def home(request, key):
    messages = Message.objects.filter(room__key=key).order_by('created_at')
    text = ""
    for message in messages:
        text+= "Anonymous: "+message.message+"\n"
        # print(message.message)
    return render(request, 'chatroom.html',{'key':key, 'text':text})


def index(request):
    
    return render(request, 'index.html')