from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

import blog
from blog.models import Blog


# Create your views here.
class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')

class BlogDeleteView(DeleteView):
    model = Blog
    #fields = ('name', 'description', 'image')
    success_url = reverse_lazy('blog:list')

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count +=1
        if self.object.view_count == 100:
            send_mail(
                subject='ПОЗДРАВЛЕНИЕ',
                message=f'Поздравляем ваш пост {self.object.name} набрал 100 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['igor.zinoviev08@yandex.ru'],
                fail_silently=False,
            )

        self.object.save()
        return self.object





