from django.shortcuts import render

# Create your views here.
def ApiIndexView(request):
    return render(request, 'api/index.html')