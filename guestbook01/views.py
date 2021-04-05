from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'guestbook01/index.html')


def deleteform(request):
    return render(request, 'guestbook01/deleteform.html')