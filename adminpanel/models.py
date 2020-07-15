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
