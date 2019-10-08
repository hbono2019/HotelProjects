from django.shortcuts import render


# Create your views here.
def HotelsApp(request):
    return render(request, 'HotelsApp.html', {})
