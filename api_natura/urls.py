from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', view=views.get_products, name='get_all_products'),
    path('products/<int:id>', view=views.get_by_id, name='get_product_by_id'),
    path('manager/', view=views.product_manager, name='product_manager'),
]