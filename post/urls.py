from django.urls import path
from .views import index, category_view, region_view, post_detail_view

urlpatterns = [
    path('', index, name='index'),
    path('cateogry/<slug:slug>/', category_view, name='category'),
    path('region/<slug:slug>/', region_view, name='region'),
    path('post/<slug:slug>/', post_detail_view, name='post_detail'),
]