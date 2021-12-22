from django.contrib import admin
from .models import CategoryDish, Dish, Ticket, Hero, Chiefs, ModelFormRegistration


@admin.register(CategoryDish)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_filter = ['position']
    list_editable = ['position']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'category', 'dish_order', 'is_special', 'ingredients', 'desc', 'price']
    list_filter = ['dish_order']
    list_editable = ['is_special', 'ingredients', 'desc', 'price']


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'ticket']
    list_filter = ['position']
    list_editable = ['ticket']


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'showtext', 'photo']
    list_filter = ['position']
    list_editable = ['showtext']


@admin.register(Chiefs)
class CheifsAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'prof', 'photo']
    list_filter = ['position']
    list_editable = ['prof']

admin.site.register(ModelFormRegistration)


