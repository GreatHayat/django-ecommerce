from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Category, Brand, Product, Images, Review
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    request.GET.get('category_id', None)
    mobile_products = Product.objects.filter(category__name__icontains="Mobile Phones").order_by("-name")[:6]
    brands = Brand.objects.all()
    featured_products = Product.objects.filter(isFeatured=True)[:6]
    promotion_product = Product.objects.filter(brand__name__icontains="apple",
                                              category__name__icontains="mobile phones",
                                              isPromotion=True)[:1]
    promotion_products = Product.objects.filter(brand__name__icontains="apple",
                                                isFeatured=True)[:4]
    context = {
        "mobile_products" : mobile_products,
        "brands" : brands,
        "featured" : featured_products,
        "promotion" : promotion_product,
        "promotions" : promotion_products
    }
    return render(request, "myapp/index.html", context)
@login_required()
def product_details(request, id):
    product = get_object_or_404(Product, id = id)
    reviews = Review.objects.filter(product__id=id)
    # throught link
    # Begin of User Comments Form Data
    if request.method == "POST":
        name = request.POST.get("name")    
        title = request.POST.get("title")    
        message = request.POST.get("message")
        user = User.objects.first()
        if request.user.is_authenticated:
            Review.objects.create(
                username = name,
                title = title,
                message = message,
                user = user,
                product = product
            )
        
            return HttpResponseRedirect(reverse("product_details", args=(id,)))
        else:
            messages.warning(request, "Please Login, in order to Submit a Review.")
            return HttpResponseRedirect(reverse('login'))
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return HttpResponseRedirect(reverse("index"))

    # End of User Comments Form Data
    context = {
        "product" : product,
        "reviews" : reviews,
        "user" : request.user
    }
    return render(request, "myapp/product_detail.html", context)

def search_products(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 4)

    try:
        paginate_products = paginator.page(page)
    except PageNotAnInteger:
        paginate_products = paginator.page(1)
    except EmptyPage:
        paginate_products = paginator.page(paginator.num_pages)

    if 'q' in request.POST:
        q = request.POST['q']
        if q:
            paginate_products = products.filter(Q(name__icontains=q)|
                                                Q(category__name__icontains=q)|
                                                Q(brand__name__icontains=q)).distinct()
    
    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         paginate_products = products.filter(Q(name__icontains=keyword) |
    #                                    Q(description__icontains=keyword)|
    #                                    Q(category__name__icontains=keyword)|
    #                                    Q(brand__name__icontains=keyword))
    # if 'price_from' in request.GET:
    #     price_from = request.GET['price_from']
    #     if price_from:
    #         paginate_products = products.filter(Q(original_price__iexact=price_from)|
    #                                    Q(discount_price__iexact=price_from))

    # if 'price_to' in request.GET:
    #     price_to = request.GET['price_to']
    #     if price_to:
    #         paginate_products = products.filter(Q(original_price__iexact=price_to)|
    #                                    Q(discount_price__iexact=price_to))    
    # counts = []
    #     #counts.update({brand.name:Product.objects.filter(brand__name__icontains=brand.name).count() })
    # total_count = 4
    # for brand in Brand.objects.all():
    #     total_count = Product.objects.filter(brand__name__icontains=brand.name).count()
    #     counts.append(total_count)

    
    context = {
        "products" : paginate_products,
        "brands" : brands,
        # "counts" : counts
    }
    return render(request, "myapp/search_results.html", context)


def test_view(request, id):
    brands = list(Product.objects.filter(brand__id__exact=id).values())[:6]
    context = {
        "brands" : brands
    }
    if request.user.is_authenticated:
        return JsonResponse(brands, safe=False)
    else:
        return HttpResponse("You Should have login in order to render this page...")

@login_required(login_url="login")
def ajax_data(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    if 'values' in request.GET:
        values = request.GET['values']
        if values:
            products = Product.objects.filter(name__icontains=values)
            print(products)
    context = {
        "products" : products,
        "brands" : brands
    }
    return render(request, "myapp/test.html", context)
