from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"search": ["like","like","like","like","like"], "like":["like","like","like","like","like"]}
    return render(request,"index.html", context)


def recommend(request):
    context = {}
    return render(request, "recommend.html", context) 