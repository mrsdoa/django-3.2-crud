from django.contrib import admin

# Register your models here.
from .models import Product, Stock


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Stock)
class TeacherAdmin(admin.ModelAdmin):
    pass
