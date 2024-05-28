from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# python manage.py runserver

# Create your views here.
context = { # context - set of varible hota hai
        'varible':"this is sent",
        'varible1':"this is varible 1",
    }
def index(request):

    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html',context)
    # return HttpResponse("this is about")
def services(request):
    return render(request,'services.html',context)
    # return HttpResponse("this is services")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        contact.save()
        messages.success(request, "Your Message has been sent.")
    return render(request,'contact.html',context)
    # return HttpResponse("this is contact")
