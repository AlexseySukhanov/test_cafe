from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator


class CategoryDish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.PositiveIntegerField(unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name


class Dish(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)
    dish_order = models.PositiveIntegerField(unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)
    ingredients = models.CharField(max_length=200)
    desc = models.CharField(unique=True, max_length=500)
    price = models.FloatField()

    class Meta:
        ordering = ('dish_order',)

    def __str__(self):
        return self.name


class ModelFormRegistration(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    date = models.DateField()
    time = models.DateTimeField()
    count_of_people = models.PositiveIntegerField()
    message = models.TextField(max_length=400, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-time',)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}'

class Ticket(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    ticket = models.TextField(max_length=400, blank=True)
    position = models.PositiveIntegerField(unique=True, db_index=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name


class Hero(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images', filename)

    name = models.CharField(max_length=50, db_index=True)
    position = models.PositiveIntegerField(unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    showtext = models.TextField(max_length=400, blank=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name

class Chiefs(models.Model):
    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/chefs', filename)

    name = models.CharField(max_length=50, db_index=True)
    position = models.PositiveIntegerField(unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    prof = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name




