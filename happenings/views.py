from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from happenings.models import Happening


def index(request):
    grouped_happenings = []

    for value, display_name in Happening.HappeningCategory.choices:
        happenings = Happening.objects.filter(category=value).order_by('-happening_created_date')
        if happenings.exists():
            grouped_happenings.append({
                "category_display": display_name,
                "happenings": happenings
            })

    context = {
        "grouped_happenings": grouped_happenings
    }

    return render(request, "happenings/index.html", context)

def details(request, happening_id):
    happening = get_object_or_404(Happening, pk=happening_id)
    return render(request, "happenings/details.html", {"happening": happening})