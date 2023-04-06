from django.shortcuts import render, redirect, HttpResponse
from django.http.response import HttpResponse
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')


def mainpage(request):
    manage_list = Manage.objects.all()
    context ={
        'manage_list' : manage_list
    }
    return render(request, 'mainpage.html', context)


def manage_items(request):
    if request.method=="POST":
        domains = request.POST['domains']
        emails = request.POST['emails']
        passwords = request.POST['passwords']
        mobile_numbers = request.POST['mobile_numbers']

        manage = Manage(domains = domains, emails = emails, passwords = passwords, hints = hints, mobile_numbers = mobile_numbers)
        manage.save()
        messages.info(request, "DATA ADDED SUCCESSFULLY")
    else:
        pass

    manage_list = Manage.objects.all()
    context = {
        'manage_list' : manage_list

    }
    return render(request, 'mainpage.html', context)
    

def delete_items(request, myid):
    manage = Manage.objects.get(id=myid)
    manage.delete()
    messages.info(request, "DATA DELETED SUCCESSFULLY")
    return redirect(mainpage)


def update_items(request, myid):
    sel_manage = Manage.objects.get(id=myid)
    manage_list = Manage.objects.all()
    context={
        'sel_manage' : sel_manage,
        'manage_list' : manage_list
    }

    return render(request, 'mainpage.html', context)

def updates(request, myid):
    manage = Manage.objects.get(id=myid)
    manage.domains = request.POST['domains']
    manage.emails = request.POST['emails']
    manage.passwords = request.POST['passwords']
    manage.mobile_numbers = request.POST['mobile_numbers']
    manage.save()
    messages.info(request, "DATA UPDATED SUCCESSFULLY")
    return redirect('mainpage')