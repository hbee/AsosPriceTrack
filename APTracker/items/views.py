from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import AddItemForm, CreateUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('items.main')

    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, "Account successfully created for " + username)
                return redirect('items.login')
        context = {'form': form}
        return render(request, 'items/register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('items.main')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('items.main')
            else:
                messages.info(request, "username or password is incorrect")

        context = {}
        return render(request, 'items/login.html', context)

@login_required(login_url='items.login')
def logoutUser(request):
    logout(request)
    return redirect('items.login')

@login_required(login_url='items.login')
def main_view(request):
    discounted_no = 0
    error = None
    current_user = User.objects.get(username=request.user)

    form = AddItemForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = current_user
                instance.save()
        except AttributeError:
            error = "Couldn't get the name or the price of the item"
        except:
            error = "Something went wrong"

    form = AddItemForm()
    qs = request.user.items.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = list()
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
        discounted_no = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'discounted_no': discounted_no,
        'form': form,
        'error': error,
    }

    return render(request, 'items/main.html', context)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'items/del_confirmation.html'
    success_url = reverse_lazy('items.main')
    login_url = 'items/login.html'

@login_required(login_url='items.login')
def update_prices(request):
    qs = Item.objects.all()
    for item in qs:
        item.save()
    return redirect("items.main")