from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

# В каталоге необходимо добавить возможность менять порядок отображения товаров:
# по названию в алфавитном порядке и по цене по убыванию и по возрастанию.

# def alphabet_sort(request):
#     template = 'catalog.html'
#     alph_sort = request.GET['sort']
#     phone_object = Phone.objects.order_by(alph_sort)
#     context = {'phones': phone_object}
#     return render(request, template, context)

# def show_catalog(request):
#     template = 'catalog.html'
#     alph_sort = request.GET['sort']
#     phone_object = Phone.objects.order_by(alph_sort)
#     context = {'phones': phone_object}
#     return render(request, template, context)

# def min_price(request):
#     template = 'catalog.html'
#     alph_sort = request.GET['sort']
#     if alph_sort == 'min_price':
#         alph_sort = 'price'
#         phone_object = Phone.objects.order_by(alph_sort)
#         context = {'phones': phone_object}
#         return render(request, template, context)
#
# def max_price(request):
#     template = 'catalog.html'
#     alph_sort = request.GET['sort']
#     if alph_sort == 'min_price':
#         alph_sort = '-price'
#         phone_object = Phone.objects.order_by(alph_sort)
#         context = {'phones': phone_object}
#         return render(request, template, context)

# def show_catalog(request):
#
#     template = 'catalog.html'
#     phone_object = Phone.objects.all()
#     context = {'phones': phone_object}
#     return render(request, template, context)

def show_catalog(request):
    template = 'catalog.html'

    phone_object = Phone.objects.all()
    indicator = str(request).split()[-1]

    if "'/catalog/'>" in indicator:

        context = {'phones': phone_object}
        return render(request, template, context)
    elif indicator == "'/catalog/?sort=name'>":
        alph_sort = request.GET['sort']
        phone_object = Phone.objects.order_by(alph_sort)
        context = {'phones': phone_object}
        return render(request, template, context)
    elif indicator == "'/catalog/?sort=max_price'>":

        alph_sort = '-price'
        phone_object = Phone.objects.order_by(alph_sort)
        context = {'phones': phone_object}
        return render(request, template, context)
    elif indicator == "'/catalog/?sort=min_price'>":

        alph_sort = 'price'
        phone_object = Phone.objects.order_by(alph_sort)
        context = {'phones': phone_object}
        return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug = slug)
    for phone in phones:
        context = {'phone': phone}
    return render(request, template, context)
