from django.shortcuts import render


def index(request):
    return render(request, 'assetsapp/index.html')