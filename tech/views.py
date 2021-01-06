from django.shortcuts import render, get_object_or_404
from.models import TechEntry


def tech_page(request):
    tech_entries = TechEntry.objects.order_by('-id')
    return render(request, 'tech/tech_page.html', {'tech_entries': tech_entries})



