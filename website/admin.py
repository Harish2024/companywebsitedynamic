from django.contrib import admin
from .models import Product,ProductAdmin
from .models import People,PeopleAdmin
# Register your models here.
admin.site.register(Product,ProductAdmin)

admin.site.register(People,PeopleAdmin)