from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Item
from .forms import AddItemForm
from django.views.generic import DeleteView

def main_view(request):
    discounted_no = 0
    error = None

    form = AddItemForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Couldn't get the name or the price of the item"
        except:
            error = "Something went wrong"

    form = AddItemForm()
    qs = Item.objects.all()
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


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'items/del_confirmation.html'
    success_url = reverse_lazy('items.main')

def update_prices(request):
    qs = Item.objects.all()
    for item in qs:
        item.save()
    return redirect("items.main")