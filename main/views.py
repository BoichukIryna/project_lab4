from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def contacts(request):
    return render(request, "main/contacts.html")

def calculate(request, age):
    # Проста формула: 200 + вік * 10
    cost = 200 + age * 10
    return render(request, "main/calculate.html", {"age": age, "cost": cost})