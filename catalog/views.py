from django.shortcuts import render

from catalog.models import Product, Contact
def home(request):
    context = {
        'title': 'SkyStore',
        'products': Product.objects.all()[:6]
    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    context = {
        'title': 'Contact',
        'address_info': Contact.objects.first()
    }
    if request.method == 'POST':
        visiter = {}
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['massage'] = request.POST.get('message', None)
        print(visiter)
    return render(request, 'catalog/contacts.html', context=context)
