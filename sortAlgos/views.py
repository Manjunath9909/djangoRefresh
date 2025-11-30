from django.shortcuts import HttpResponse
from algorithms.compareSortingAlgos import handler

# Create your views here.
def homePageEmpty(request):
    return HttpResponse("<h3>congrats on find the empty page stupid<h3>")

def sortingPage(request):
    numbers = request.GET.get("numbers", None)
    #print(numbers)
    dataToSort = list(map(int, numbers.split(',')))
    returnJson = handler(1, dataToSort)
    return HttpResponse(returnJson, content_type="application/json")