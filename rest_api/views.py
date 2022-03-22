from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question

# Create your views here.
def index(request, year):
    # return HttpResponse("Hello, world. You're at the polls index.")

    a_list = Question.objects.filter(pub_date__year=year)
    b_list = Choice.objects.filter(a_list)
    context = {'year': year, 'choice_list': b_list}
    return render(request, "templates/year_archive.html")