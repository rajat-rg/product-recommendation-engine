from django.contrib import admin
from products.models import products_model, userHistory
# Register your models here.
admin.site.register(products_model)
admin.site.register(userHistory)