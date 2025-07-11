from django.shortcuts import render

def get_home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')