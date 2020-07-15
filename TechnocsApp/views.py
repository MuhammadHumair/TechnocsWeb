from django.shortcuts import render, redirect
from adminpanel.models import Inquiry
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        dealed = False

        result = Inquiry.objects.create(name=name, email=email, phone=phone, subject=subject, message=message, isDealed=dealed)
        result.save()
        messages.success(request, 'Congratulations! Your inquiry successfully submitted.')
        return redirect('contact')
    else:
        return render(request, 'contact.html')

def career(request):
    return render(request, 'career.html')

def clients(request):
    return render(request, 'clients.html')

def faqs(request):
    return render(request, 'faq.html')

def team(request):
    return render(request, 'team.html')

