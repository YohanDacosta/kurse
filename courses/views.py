from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from .models import Course

# Create your views here.

class CourseListView(ListView):
    model = Course
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        
        print(context)
        
        return context