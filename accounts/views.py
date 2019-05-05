from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f"An Account Has Been Registered For {username}")
            return HttpResponseRedirect(reverse("login"))
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

    
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # login(request, user)
        return HttpResponse("Successfull")
    else:
        messages.error(request, f"Invalid Credentials for {username}")
        return render(request, "accounts/login_view.html", {})


@login_required 
def profile(request):
    context = {
        "message" : "Welcome!"
    }
    return render(request, "accounts/profile.html", context)


def username_check(request):
    username = request.POST.get("username")
    users =  User.objects.filter(username__iexact=username)
    data = {"is_exist": False}
    if users.count():
        data['is_exist'] = True
        data["error_message"] = "A username already exist with that name"
    else:
        data["is_exist"] = False
        data["success_message"] = "Username Available"
    
    return JsonResponse(data, safe=False)