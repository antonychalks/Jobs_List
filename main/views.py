from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from .models import UserProfile
from tradesman.models import Job, Task
from .forms import InitialSignUpForm


# Create your views here.
def landing_page(request):
    """ Renders the landing page of the website."""
    # Retrieve the user's profile if the user is authenticated.
    user_profile = None
    if request.user.is_authenticated:
        # Redirects the user if they haven't completed the initial signup.
        if request.user.user_profile.is_initial_signup:
            return redirect('user_profile_signup')
        else:
            user_profile = UserProfile.objects.get(user=request.user)

    return render(
        request,
        "main/index.html",
        {
            "user_profile": user_profile,
            "job": Job,
            "task": Task,
        },
    )


def user_profile_signup(request):
    """A page where the user can complete some sign up fields"""
    user = request.user
    form = InitialSignUpForm(request.POST, instance=user.user_profile)

    # Saves the initial signup page form if the form is valid.
    if request.method == "POST":
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.is_initial_signup = False
            user_profile.save()
            messages.success(request, 'New User Added!')
            # If the user selects "Continue Later", they will be redirected to the home page.
            if "continue_later" in request.POST:
                return redirect(reverse('home'))
            # If the user selects "Add More Details", they will be redirected to the user detail page.
            elif "more_details" in request.POST:
                return redirect(reverse('user_detail', kwargs={'slug': user.user_profile.slug}))

    return render(
        request,
        "main/user_profile_signup.html",
        {
            "user": user,
            "form": form,
        }
    )
