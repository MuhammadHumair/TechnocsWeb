from django.shortcuts import render, redirect
from adminpanel.models import *
from django.contrib import messages
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


def categoryTags(request):
    if request.method == "POST":
        catname = request.POST["tagname"]
        cattitle = request.POST["tagtitle"]
        status = request.POST["isActive"]
        if status == "on":
            status = True
        else:
            status = False
        query = ServiceCategories.objects.create(categoryName=catname, categoryTitle=cattitle, isActive=status)
        query.save()
        return redirect('categoryTags')
    else:
        tag_data = ServiceCategories.objects.all().order_by('categoryName')
    return render(request, 'adminpanel/category_tags.html', {'categoryTags': tag_data})


def category(request):
    if request.method == "POST":
        cattag = request.POST["categorytag"]
        cattitle = request.POST["categorytitle"]
        catimg = request.FILES["image"]
        status = request.POST["isActive"]
        if status == "on":
            status = True
        else:
            status = False
        
        query = ServiceSubCategories.objects.create(category_id=cattag, subCategoryTitle=cattitle, image=catimg, isActive=status)
        query.save()
        return redirect('category')
    else:
        categories = ServiceSubCategories.objects.all()
        tags = ServiceCategories.objects.all()
    return render(request, 'adminpanel/category.html',{'categories':categories,'tags':tags})

def tagStatus(request, status, id):
    if status == 'Hide':
        tag = ServiceCategories.objects.filter(id=id)
        tag.update(isActive=False)
        category = ServiceSubCategories.objects.filter(category_id=id)
        category.update(isActive=False)
        return redirect('categoryTags')
    else:
        ServiceCategories.objects.filter(id=id).update(isActive=True)
        ServiceSubCategories.objects.filter(
            category_id=id).update(isActive=True)
        return redirect('categoryTags')


def tagCategoryStatus(request, status, id):
    if status == 'Hide':
        ServiceSubCategories.objects.filter(category_id=id).update(isActive=False)
        return redirect('category')
    else:
        cat = ServiceCategories.objects.get(id=id)
        if str(cat.isActive) == 'True':
            ServiceSubCategories.objects.filter(category_id=id).update(isActive=True)
        else:
            messages.error(request,'Firstly, Activate the Tag for this category. It cannot show because its category tag is hide.')
        return redirect('category')

def services(request):
    return render(request, 'adminpanel/services.html')

def projects(request):
    return render(request, 'adminpanel/projects.html')

def clients(request):
    if request.method == 'POST':
        logo = request.FILES['clientlogo']
        status = request.POST["isActive"]
        if status == "on":
            status = True
        else:
            status = False

        query = Clients.objects.create(clientLogo=logo, isActive=status)
        query.save()
        return redirect('clients')
    else:
        clients = Clients.objects.all()
    return render(request, 'adminpanel/clients.html', {'clients': clients})

def clientStatus(request, status, id):
    if status == 'Hide':
        client = Clients.objects.filter(id=id)
        client.update(isActive=False)
        return redirect('clients')
    else:
        Clients.objects.filter(id=id).update(isActive=True)
        return redirect('clients')

def team(request):
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        img = request.FILES['picture']
        status = request.POST["isActive"]
        if status == "on":
            status = True
        else:
            status = False

        query = Team.objects.create(name=name, designation=designation, image=img, isActive=status)
        query.save()
        return redirect('team')
    else:
        teams = Team.objects.all()
    return render(request, 'adminpanel/team.html',{'teams':teams})
    

def teamStatus(request, status, id):
    if status == 'Hide':
        team = Team.objects.filter(id=id)
        team.update(isActive=False)
        return redirect('team')
    else:
        Team.objects.filter(id=id).update(isActive=True)
        return redirect('team')
