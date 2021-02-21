# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Harish Electronic Private Limited
    </div></title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/img/title.jng' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        harish Electronic Private Limited.
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contact">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Harishs Electronic Private Limited, Developed by Harisf G.
    </div>
    </div>
</body>

</html>
```

### home.html:
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building2.jpeg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}
```

### product.html:
```
{% extends "website/base.html" %}

{% block content %}
<div class="productcontent">    
    <h1 style="text-align:center;"><u>Our Premium Products</u></h1>
    <div class="productitems">
    {% for product in products  %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{ product.photo.url }}" alt="product image">
            </div>
            <div class="Itemname">Name:{{ product.Itemname }}</div>
            <div class="Product price">Price:{{ product.Price }}</div>
        </div>
    {% endfor %}
    </div>
</div>
{% endblock  %}
```

### people.html:
```
{% extends "website/base.html" %}

{% block content %}
    <h1 id="Ex">Executives</h1>
    {% for people in peoples %}
        <div class="productitem"> 
            <div class="itemimage">
            <img src="{{ people.photo.url }}" alt="executive image" width="250" height="200">
            </div>
            <div class="Itemname">Name:{{ people.Membername }}</div>
            <div class="Product price">Designation:{{ people.Designation }}</div>
        </div>
    {% endfor %}
    </div>
</div>
{% endblock  %}
```

### contact.html:
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecont">    
    <h1>Contact Us</h1>
    
    <div class="contenttext">
    <p style="font-size:30px">email : harishelectroniclimited@gmail.com</p>
    <p style="font-size:30px">ph.no : +91 44456 77789    +91 88856 00075</p>
    
    </div>
    </div>
{% endblock  %}
```

### admiin.py:
```
from django.contrib import admin
from .models import Product,ProductAdmin
from .models import People,PeopleAdmin
# Register your models here.
admin.site.register(Product,ProductAdmin)

admin.site.register(People,PeopleAdmin)
```

### models.py
```
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

```

## OUTPUT:
![output](./static/img/1.PNG)

![output](./static/img/2.PNG)

![output](./static/img/3.PNG)

![output](./static/img/4.PNG)

### ADMIN PAGE:

![output](./static/img/5.PNG)

![output](./static/img/6.PNG)

## CODE VALIDAOR:
![output](./static/img/7.PNG)

![output](./static/img/8.PNG)

![output](./static/img/9.PNG)

![output](./static/img/10.PNG)

## RESULT:
Thus a website is designed for the manufacturing company and is hosted in the URL http://harish.student.saveetha.in:8000/.