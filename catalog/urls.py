from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ContactDetailView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<str:name>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/<str:name>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<str:name>/delete/', ProductDeleteView.as_view(), name='product_delete'),

]
