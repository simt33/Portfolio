from django.shortcuts import render, get_object_or_404
from.models import JobEntry


def jobs_page(request):
    jobs = JobEntry.objects
    return render(request, 'jobs/jobs_page.html', {'jobs': jobs})
