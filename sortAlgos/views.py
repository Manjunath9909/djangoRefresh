from django.shortcuts import render
from django.shortcuts import HttpResponse, render
from algorithms.compareSortingAlgos import handler

# Create your views here.
def homePageEmpty(request):
    return HttpResponse("<h3>congrats on find the empty page stupid<h3>")

def sortingPage(request):
    numbers = request.GET.get("numbers", "NONE")
    print(numbers)
    
    #sortType= request.GET.get("type", 1)
    return HttpResponse("<h1>" + handler(1, numbers) + "</h1>")