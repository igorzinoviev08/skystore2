from django.db import models
from pytils.translit import slugify

class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.SlugField(max_lenght=100, verbose_name='slug', unique=True)
    description =models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение')
    issued_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        return  f'{self.name}'

    def save(self, *aegs, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(args, **kwargs)








# # Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Product(models.Model):
#     class Meta:
#         ordering = ['-created_at']
#
#
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     preview_description = models.TextField()
#     image = models.ImageField(upload_to='products_images')
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     last_modified = models.DateTimeField(auto_now_add=True)
#
#
#
#     def __str__(self):
#         return f"Product(pk={self.pk}, name={self.name!r}"
#
#     def get_preview_description(self):
#         return self.preview_description.split('-')[1:]
#
#
# class Contact(models.Model):
#     country = models.CharField(max_length=100)
#     inn = models.CharField(max_length=18)
#     address = models.CharField(max_length=200)
#
#     def __str__(self):
#         return f"{self.country} {self.address}"
