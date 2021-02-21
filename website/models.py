from django.db import models
from django.contrib import admin

# Create your models here.
class Product(models.Model):
    Itemname = models.CharField(max_length=100)
    Price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Itemname','Price','photo')

class People(models.Model):
    Membername = models.CharField(max_length=100)
    Designation = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photos/')

class PeopleAdmin(admin.ModelAdmin) :
    list_display = ('Membername','Designation', 'photo')
