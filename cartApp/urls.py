from django.urls import path
from . import views
urlpatterns = [
    path("home", views.home, name="home"),
    # path("cart-index", views.index, name="cart-index")
]