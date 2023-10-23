from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

import blog
from catalog.models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ContactsListView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'
    context_object_name = 'address_info'
    queryset = Contact.objects.all()





