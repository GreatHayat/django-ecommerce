from django.shortcuts import render
# from .models import Cart
# # Create your views here.

# def index(request):
#     cart_id = request.session.get("cart_id", None)
#     if cart_id is None and isinstance(cart_id, int):
#         cart_obj = Cart.objects.create(user=None)
#         request.session['cart_id'] = cart_obj.id
#         print("New Cart ID Created")
#     else:
#         print("Cart Already Exist")
#         print(cart_id)
    
#     context = {
#         "message" : "Cart App!"
#     }
#     return render(request, "cartApp/home.html", context)


def home(request):
    my_car = request.session['my_car'] = "Toyota"
    toyota = request.session.get("my_car")
    print(toyota)
    try:
        del request.session['my_car']
    except KeyError:
        print("Key Doesn't Exist")
    context = {
        "message" : "Cart App!"
    }
    return render(request, "cartApp/home.html", context)