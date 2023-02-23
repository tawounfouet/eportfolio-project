from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def home(request):
    #return HttpResponse("<h1>Home page<h1>")
    return render(request, 'projects/project_list.html')