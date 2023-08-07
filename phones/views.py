from django.shortcuts import render, redirect
from phones.models import Phone




def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_object = Phone.objects.all()
    return render(request, template, {'phones': phone_object})



def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug = slug)
    for phone in phones:
        context ={'phone':phone}

    return render(request, template, context)
