from django.shortcuts import render
from django.views import generic
from .models import Job
from django.contrib import messages


# Create your views here.
class tradesman_home(generic.ListView):
    queryset = Job.objects.all()
    template_name = "planners/tradesman_home.html"
    paginate_by = 6
    
def view_job(request):
        return render(
        request,
        "tradesman/job_detail.html",
    )