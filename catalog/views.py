from django.conf import settings
from django.views.generic import ListView

import blog


class BlogListView(ListView):
    model = blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogCreateView(CreateView):
    model = blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lasy('blog:list')

class BlogUpdateView(UpdateView):
    model = blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lasy('blog:list')

class BlogDeleteView(DeleteView):
    model = blog
    #fields = ('name', 'description', 'image')
    success_url = reverse_lasy('blog:list')

class BlogDetailView(DetailView):
    model = blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count +=1
        if self.object.view_count == 100
            send_mail(
                subject='ПОЗДРАВЛЕНИЕ',
                message=f'Поздравляем ваш пост {self.object.name} набрал 100 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['igor.zinoviev08@yandex.ru'],
                fail_silently=False,
            )

        self.object.save()
        return self.object









#from catalog.models import Product, Contact













class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'
    queryset = Product.objects.all()[:6]

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

class ContactsListView(ListView):
    model = Contact
    template_name = 'catalog/contacts.html'
    context_object_name = 'address_info'
    queryset = Contact.objects.first()





