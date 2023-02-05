from django.shortcuts import render, HttpResponse
from .models import Category, Dish


def main_page(request):
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
    })
