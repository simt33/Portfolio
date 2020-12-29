from django.shortcuts import render, get_object_or_404
from.models import JobEntry


def profile_page(request):

    return render(request, 'profile/profile_page.html')
