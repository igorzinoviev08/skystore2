from django.urls import path
from blog.views import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<slug>', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug>', BlogDeleteView.as_view(), name='delete'),
    path('detail/<slug>', BlogDetailView.as_view(), name='detail),

]