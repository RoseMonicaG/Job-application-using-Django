from django.shortcuts import render
from .forms import JobApplicationForm

def job_application_view(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return ('success')
    else:
        form = JobApplicationForm()
    return render(request, 'applications/job_application.html', {'form': form})


