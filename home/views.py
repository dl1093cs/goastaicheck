from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
    # Extract 'x' from request parameters
    try:
        x = int(request.GET.get('x', 0))  # Assuming 'x' is passed as a GET parameter
    except (ValueError, TypeError):
        raise Http404("Parameter 'x' is not an integer or is missing.")

    # Check if 'x' is greater than 0 and render the appropriate template
    if x > 0:
        return render(request, "x_greater_index.html")
    else:
        return render(request, "x_lower_index.html")