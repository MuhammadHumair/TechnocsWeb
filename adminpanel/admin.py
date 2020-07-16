from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Faqs)
admin.site.register(Inquiry)
admin.site.register(Services)
admin.site.register(ServiceCategories)
admin.site.register(ServiceSubCategories)