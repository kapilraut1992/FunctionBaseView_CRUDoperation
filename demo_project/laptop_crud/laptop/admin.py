from django.contrib import admin
from .models import Laptop

# Register your models here.
class laptopAdmin(admin.ModelAdmin):
    list_display=['id','model_name','ram','rom','processor','price','weight']

admin.site.register(Laptop,laptopAdmin)
