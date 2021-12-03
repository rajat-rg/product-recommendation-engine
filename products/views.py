from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import products_model, userHistory
import pickle
# Create your views here.

products = products_model.objects.all()
similarity = pickle.load(open('similarity.pkl','rb'))

def index(request):
    searches = userHistory.objects.filter(user=request.user)[::-1]
    if len(searches)>=5:
        searches = searches[0:5]
    famous = products_model.objects.all().order_by('-views')[:5]
    context = {"search": searches, "famous":famous}
    return render(request,"index.html", context)


def recommendations(request):
    context = {}
    if request.method == "GET":

        if 'term' in request.GET:
            qs = products_model.objects.filter(name__contains=request.GET.get('term'))
            products = list()
            for product in qs:
                products.append(product.name)
            return JsonResponse(products, safe=False)

        searched_product = request.GET.get("search")

        if searched_product == "":
            return redirect("Home")
        product = products_model.objects.all().filter(name = searched_product)[0]
        product_index = product.id -1
        searched_product = products_model.objects.get(id = product_index+1)
        searched_product.views = searched_product.views+1
        searched_product.save()
        if request.user is not None:
            history = userHistory(user=request.user, product=searched_product)
            history.save()
        distances = similarity[product_index][1]
        product_list = sorted(list(enumerate(distances)), reverse= True, key = lambda x: x[1])[1:6]
        product_recommended = list()
        for i in product_list:
            x =products_model.objects.get(id= i[0]+1)
            product_recommended.append(x)  
        context = {"product": searched_product,"recommendations": product_recommended}        
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
            messages.success(request, "Logged in !!")
            return redirect("Home")
        else:
            messages.warning(request, "Youre not recognized !!")
    return redirect("Home")

def handleLogout(request):
    logout(request)
    return redirect("Home")


# trolly
# trolly1234