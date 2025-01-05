from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here

# admin.py

from django.contrib import admin
from .models import CarMake, CarModel

# Inline configuration for CarModel (display related CarModels inside the CarMake form)
class CarModelInline(admin.TabularInline):
    model = CarModel  # Specify the related model
    extra = 1  # Add one empty form by default to add new CarModel
    fields = ['name', 'type', 'year']  # Display the name, type, and year of CarModel in the inline form

# Admin class for CarMake
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # List the 'name' and 'description' fields
    search_fields = ['name']  # Enable search by 'name'
    inlines = [CarModelInline]  # Embed CarModelInline inside CarMake's admin page

# Admin class for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')  # Show model name, car make, type, and year in the list
    list_filter = ('car_make', 'type')  # Filter by car make and type
    search_fields = ['name']  # Enable search by 'name'

# Register the models with the admin interface
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
