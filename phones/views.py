from django.shortcuts import render, redirect
from phones.models import Phone


# phone_object = phones_phone.objects.all()
# print(phone_object)
def index(request):
    return redirect('catalog')


# {self.name}{self.price}{self.image}{self.release_date}{self.lte_exists}{self.slug}
def show_catalog(request):
    template = 'catalog.html'
    # context = {'phones': phones_list}

    phone_object = Phone.objects.all()
    for phones in phone_object:
        phones_list = [phones]
        # context = {'phones': phones}
        context = {'phones': phones_list}
    # print('_____')
    # print(context)
    # print('______')
        return render(request, template, context)


    #     print(phones)
    #     print(type(phones))
    #     print("SEX")
    #     context = {'id': phones.id,
    #            'name': phones.name,
    #            'price': phones.price,
    #            'image': phones.image,
    #            'release_date': phones.release_date,
    #            'lte_exists': phones.lte_exists,
    #             'slug': phones.slug}
    # #     print(f'__________{phones}_______')
    # #     context = {phones}




# print(phone_object)
# print('___________________________')
# for object in phone_object:
#     print(f'this is object{object}')
#     context = {'id': object.id,
#                'name': object.name,
#                'price': object.price,
#                'image': object.image,
#                'release_date': object.release_date,
#                'lte_exists': object.lte_exists,
#                'slug': object.slug}
#     print("___________")
#     print(context)
#     print("___________")


# context = {'id': object['id'],
#            'name': object['name'],
#             'price': object['price'],
#             'image': object['image'],
#             'release_date': object['release_date'],
#             'lte_exists': object['lte_exists'],
#            'slug': object['slug']
#            }

# context ={'phone': object}

# print("Sex with men")
# print(context)
# context = {'name': object.name,
#            'price': object.price,
#            'image': object.image,
#            'release_date': object.release_date,
#            'lte_exists': object.lte_exists}
# print("Second sex")
# print(context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
