from django.shortcuts import render

from main.forms import InspectionUploadForm
from main.models import InspectionUpload


def index(request):

    if request.method == "POST":
        form = InspectionUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_file in request.FILES.getlist('inspection_file'):
                InspectionUpload.objects.create(
                    agent_email=form.cleaned_data['agent_email'],
                    inspection_file=uploaded_file
                )
            return render(request, 'main/thanks.html')

    else:
        form = InspectionUploadForm()
    return render(request, 'main/index.html', {'form': form})
