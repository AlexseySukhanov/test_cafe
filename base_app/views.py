from django.shortcuts import render, redirect
from .models import Dish, CategoryDish, Ticket, Chiefs
from .forms import FormRegistration


def base_app_view(request):
    if request.method == 'POST':
        form = FormRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    form_registration = FormRegistration()
    dish = Dish.objects.filter(is_visible=True).order_by('-dish_order')
    categories = CategoryDish.objects.filter(is_visible=True).order_by('position')
    special = Dish.objects.filter(is_special=True, is_visible=True)
    tickets = Ticket.objects.all()
    chiefs = Chiefs.objects.all()
    return render(request, 'base_app.html', context={
        'dishes': dish,
        'categories': categories,
        'special': special,
        'tickets': tickets,
        'chiefs': chiefs,
        'form_registration':form_registration,
    })
