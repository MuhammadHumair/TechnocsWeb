from django.shortcuts import render, redirect
from .models import Faqs, Inquiry
import datetime

# Create your views here.

def index(request):
    if 'username' in request.session:
        return render(request, "adminpanel/index.html")
    else:
        return redirect('/account/login')

def faqs(request):
    if request.method == "POST":
        q = request.POST['question']
        a = request.POST['answer']
        status = request.POST['isActive']
        if status == 'on':
            status = True
        else:
            status = False
        result = Faqs.objects.create(question=q, answer=a, isActive=status)
        result.save()
        return redirect('faqs') 
    else:
        faq_data = Faqs.objects.all()

    return render(request, 'adminpanel/faqs.html', {'faqs': faq_data})

def editFaq(request, id):
    if request.method == "POST":
        q = request.POST['question']
        a = request.POST['answer']
        Faqs.objects.filter(id=id).update(question=q, answer=a)
        return redirect('faqs')
    else:
        efaq = Faqs.objects.get(id=id)
    return render(request, 'adminpanel/edit_faq.html', {'efaqs': efaq})

def faqStatus(request, status, id):
    if status == 'active':
        faq = Faqs.objects.filter(id=id)
        faq.update(isActive=True)
        return redirect('faqs')
    else:
        Faqs.objects.filter(id=id).update(isActive=False)
        return redirect('faqs')

def inquiry(request):
    inquiry_data = Inquiry.objects.all()
    return render(request, 'adminpanel/inquiry.html', {'inquiries':inquiry_data})


def inquiryStatus(request, status, id):
    if status == 'undealed':
        inquiry = Inquiry.objects.filter(id=id)
        inquiry.update(isDealed=False, dealedDate=None)
        return redirect('inquiry')
    else:
        Inquiry.objects.filter(id=id).update(isDealed=True, dealedDate=datetime.date.today())
        return redirect('inquiry')

def services(request):
    return render(request, 'adminpanel/services.html')

def projects(request):
    return render(request, 'adminpanel/projects.html')
