from django.shortcuts import render

from main.models import HomeBuyer


def index(request):

    if request.method == "POST":
        HomeBuyer.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            current_address=request.POST['current_address'],
            property_address=request.POST['property_address'],
        )

    return render(request, 'main/index.html', {})
