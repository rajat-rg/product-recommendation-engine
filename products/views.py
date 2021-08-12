from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    context = {"search": ["like","like","like","like","like"], "like":["like","like","like","like","like"]}
    return render(request,"index.html", context)


def recommend(request):
    context = {}
    return render(request, "recommend.html", context) 

def handleSignup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1, first_name = fname, last_name = lname)
            user.save()
        else:
            messages.info(request, "Password didn't matched !!")

    return redirect("Home")

def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get("loginusername")
        password = request.POST.get("loginpassword")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            messages.warning(request, "Youre not recognized !!")
    return render("index.html")
