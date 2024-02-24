from django.shortcuts import render
from .models import UserProfile

# Create your views here.
def landing_page(request):
    
    return render(
        request,
        "main/index.html",
        {
            "UserProfile": UserProfile,
        },
    )