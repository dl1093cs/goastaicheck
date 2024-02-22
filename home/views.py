from django.shortcuts import render

# Create your views here.
def index(request):
    if x > 0:
        return render(request, "x_greater_index.html", context={})
    else:
        return render(request, "x_lower_index.html", context={})