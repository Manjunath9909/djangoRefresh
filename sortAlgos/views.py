from django.shortcuts import render
from django.shortcuts import HttpResponse, render
from algorithms.compareSortingAlgos import handler

# Create your views here.
def homePageEmpty(request):
    return HttpResponse("<h3>congrats on find the empty page stupid<h3>")

def sortingPage(request):
    return HttpResponse("<h3>Hello stupid world!! this is a page for a sorting algorithms<h3>")