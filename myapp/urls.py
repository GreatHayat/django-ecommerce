from django.urls import path
from . import views
urlpatterns = [
    path("index", views.index, name="index"),
    path("details/<int:id>", views.product_details, name="product_details"),
    path("products", views.search_products, name="products"),
    path('test/<int:id>', views.test_view, name="test_view"),
    path("ajax", views.ajax_data, name="ajax_data")
]