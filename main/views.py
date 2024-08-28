from django.shortcuts import render
from .models import UserProfile
from tradesman.models import Job, Task


# Create your views here.
def landing_page(request):
    # Retrieve the user's profile if the user is authenticated
    user_profile = None
    # if request.user.is_authenticated:
    #     user_profile = UserProfile.objects.get(user=request.user)

    return render(
        request,
        "main/index.html",
        {
            "user_profile": user_profile,
            "job": Job,
            "task": Task,
        },
    )