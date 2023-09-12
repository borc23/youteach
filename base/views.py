from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Lets learn C++!'},
    {'id': 2, 'name': 'Lets learn JavaScript!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room(request):
    return render(request, 'room.html')