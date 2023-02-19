from django.shortcuts import render, redirect
from .models import Category, Dish
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def main_page(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    reservation_form = ReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'reservation_form': reservation_form,
    })
