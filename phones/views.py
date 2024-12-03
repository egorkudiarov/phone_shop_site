from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Phone

def show_catalog(request):
    template = 'catalog.html'

    page_num = int(request.GET.get('page', 1))
    page_lot = int(request.GET.get('lots', 10))
    page_sort = request.GET.get('sort', '') 

    phone_objects = [phone for phone in Phone.objects.all()]
    match page_sort:
        case 'name':
            phone_objects.sort(key=lambda phone: phone.name)
        case 'min_price':
            phone_objects.sort(key=lambda phone: phone.price)
        case 'max_price':
            phone_objects.sort(key=lambda phone: phone.price, reverse=True)
        
    paginator = Paginator(phone_objects, page_lot)
    page = paginator.get_page(page_num)

    context = {
        'page': page
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone_objects = Phone.objects.filter(slug=slug)
    phone_object = phone_objects.get()

    context = {
        'phone': phone_object,
    }
    return render(request, template, context)

