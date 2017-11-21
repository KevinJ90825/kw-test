import housecanary
from django.shortcuts import render
from django.conf import settings
from main.models import HomeBuyer


def index(request):

    if request.method == "POST":
        client = housecanary.ApiClient(settings.CANARY_KEY, settings.CANARY_SECRET)
        response = client.property.value((request.POST['property_address']))
        HomeBuyer.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            current_address=request.POST['current_address'],
            property_address=request.POST['property_address'],
            housecanary=response.json()
        )

    return render(request, 'main/index.html', {})
