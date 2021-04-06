from django.http import HttpResponseRedirect
from django.shortcuts import render

import guestbook01.models as guestbookmodel


def index(request):
    results = guestbookmodel.findall()
    data = {'guestbooklist': results}
    return render(request, 'guestbook01/index.html', data)


def add(request):
    name = request.POST['name']
    password = request.POST['password']
    message = request.POST['message']

    guestbookmodel.insert(name, password, message)

    return HttpResponseRedirect('/guestbook01')


def deleteform(request):
    return render(request, 'guestbook01/deleteform.html')


def delete(request):
    no = request.POST['no']
    password = request.POST['password']

    guestbookmodel.deleteby_no_and_password(no, password)

    return HttpResponseRedirect('/guestbook01')