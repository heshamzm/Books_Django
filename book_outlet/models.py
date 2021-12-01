from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}, {self.code}"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Adress Entires"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null= True) #one to one relationship

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True, related_name="books") #one to many relationship
    is_best = models.BooleanField(default= False)
    slug = models.SlugField(default="", blank=True, db_index=True)
    published_countries = models.ManyToManyField(Country) #many to many relationship

    # def save(self, *args, **kwargs): >> this function ovvride the name of the slug to be the title
    #     self.slug = slugify(self.title)
    #     super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f" Name: {self.title}, Rating: ({self.rating}), author: {self.author}, Is the best selling: {self.is_best}."
