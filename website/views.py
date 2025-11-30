from django.shortcuts import render, HttpResponse

def renderSortingPage(request):
    return render(request, "index.html")