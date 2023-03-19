from django.shortcuts import render


# displays index.html
def home_response(request):
    return render(request, 'index.html')
