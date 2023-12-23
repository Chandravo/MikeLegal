from django.shortcuts import render

# Create your views here.
def home(request, key):
    
    return render(request, 'chatroom.html',{'key':key})


def index(request):
    
    return render(request, 'index.html')