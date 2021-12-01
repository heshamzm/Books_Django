from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Book, Author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin): #configure adminstration fields
    
    prepopulated_fields = {"slug":("title",)} # this filed to fullfiled the slug field automaticly
    list_filter = ("author", "rating",) # this field to display filters in the admin panel
    list_display = ("title", "author") # this filed is how to display the columns in the admin panel for each table.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name", "address") # this filed is how to display the columns in the admin panel for each table.


# register the models to be shown in the admin.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)