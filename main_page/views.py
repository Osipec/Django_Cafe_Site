from django.shortcuts import render, redirect
from .models import Category, Dish, TableReserv
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


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
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'reservation_form': reservation_form,
        'user_manager': user_manager,
        'user_auth': user_auth
    })


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    TableReserv.objects.filter(pk=pk).update(processed=True)
    return redirect('main_page:list_reservations')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def list_reservations(request):
    messages = TableReserv.objects.filter(processed=False)
    return render(request, 'reservations.html', context={'reservations': messages})
