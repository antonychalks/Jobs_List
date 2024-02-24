from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from main.models import UserProfile as UserProfile
from django.contrib.auth.models import User

# Create your views here.
def planner_home(request):
    return render(
        request,
        "planners/planner_home.html",
    )
    
class UserList(generic.ListView):
    queryset = UserProfile.objects.all()
    context_object_name = 'UserList'
    template_name = "planners/list_tradesman.html"
    paginate_by = 6


def user_detail(request, slug):
    queryset = UserProfile.objects.all()

    user = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "planners/user_detail.html",
        {
            "user": user,
        },
    )