from django.shortcuts import render

# Create your views here.
def tradesman_home(request):
    return render(
        request,
        "tradesman/home.html",
    )