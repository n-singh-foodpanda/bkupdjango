from django.shortcuts import render


# Create your views here.

def myview(request):
    return render(request, 'personal/my.html')
