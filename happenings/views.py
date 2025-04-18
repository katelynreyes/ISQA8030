from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from happenings.models import Happening


def index(request):
    all_happenings = Happening.objects.order_by('happening_created_date')
    context = {"all_happenings": all_happenings}
    return render(request, "happenings/index.html", context)

def details(request, happening_id):
    happening = get_object_or_404(Happening, pk=happening_id)
    return render(request, "happenings/details.html", {"happening": happening})