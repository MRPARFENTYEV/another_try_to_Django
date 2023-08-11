from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'

    phone_object = Phone.objects.all()
    indicator = str(request).split()[-1]
    beta_sort = request.GET.get('sort')

    if beta_sort is None:
        context = {'phones': phone_object}
        return render(request, template, context)
    elif beta_sort == "name":
        phone_object = Phone.objects.order_by(beta_sort)
        context = {'phones': phone_object}
        return render(request, template, context)
    elif beta_sort == "max_price":
        beta_sort = '-price'
        phone_object = Phone.objects.order_by(beta_sort)
        context = {'phones': phone_object}
        return render(request, template, context)
    elif beta_sort == "min_price":
        beta_sort = 'price'
        phone_object = Phone.objects.order_by(beta_sort)
        context = {'phones': phone_object}
        return render(request, template, context)


# def show_catalog(request):
#     template = 'catalog.html'
#
#     phone_object = Phone.objects.all()
#     indicator = str(request).split()[-1]
#     beta_sort = request.GET.get('sort')
#
#     if "'/catalog/'>" in indicator:
#
#         context = {'phones': phone_object}
#         return render(request, template, context)
#     elif indicator == "'/catalog/?sort=name'>":
#         alph_sort = request.GET['sort']
#         print(beta_sort)
#         phone_object = Phone.objects.order_by(alph_sort)
#         context = {'phones': phone_object}
#         return render(request, template, context)
#     elif indicator == "'/catalog/?sort=max_price'>":
#         print(beta_sort)
#         alph_sort = '-price'
#         phone_object = Phone.objects.order_by(alph_sort)
#         context = {'phones': phone_object}
#         return render(request, template, context)
#     elif indicator == "'/catalog/?sort=min_price'>":
#         print(beta_sort)
#         alph_sort = 'price'
#         phone_object = Phone.objects.order_by(alph_sort)
#         context = {'phones': phone_object}
#         return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug = slug)
    for phone in phones:
        context = {'phone': phone}
    return render(request, template, context)
