from django.db import models

# Create your models here.

class Faqs(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    isActive = models.BooleanField()

    def __str__(self):
        return self.question

    class Meta:
        db_table = 'Faqs'
    

class Inquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.BigIntegerField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    inquiryDate = models.DateField(auto_now=True)
    dealedDate = models.DateField(null=True, blank=True)
    isDealed = models.BooleanField()

    def __str__(self):
        return self.name +" -> "+ self.subject
    
    class Meta:
        db_table = 'Inquiry'

class ServiceCategories(models.Model):
    categoryName = models.CharField(max_length=50)
    categoryTitle = models.CharField(max_length=50)
    isActive = models.BooleanField()

    def __str__(self):
        return self.categoryName

    class Meta:
        db_table = 'ServiceCategories'

class ServiceSubCategories(models.Model):
    category = models.ForeignKey(ServiceCategories, related_name='subcategory', on_delete=models.CASCADE)
    subCategoryTitle = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='static/uploads/categories', height_field=None, width_field=None, max_length=None)
    isActive = models.BooleanField()

    class Meta:
        db_table = 'ServiceSubCategories'

class Services(models.Model):
    serviceTitle = models.CharField(max_length=50)
    descriptionTitle = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    technologies = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to='static/uploads/services', height_field=None,
                                width_field=None, max_length=None)
    image2 = models.ImageField(upload_to='static/uploads/services', height_field=None,
                               width_field=None, max_length=None, blank=True, null=True)
    image3 = models.ImageField(upload_to='static/uploads/services', height_field=None,
                               width_field=None, max_length=None, blank=True, null=True)
    contactTitle = models.CharField(max_length=50)
    filedTitle = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=100)
    contactPhone = models.BigIntegerField()
    contactEmail = models.EmailField(max_length=150)
    isActive = models.BooleanField()

    def __str__(self):
        return self.serviceTitle

    class Meta:
        db_table = 'Services'
    
    
