from django.shortcuts import render
from listings.models import SearchLog
from datetime import datetime

def reports_home(request):
    year = request.GET.get("year")
    month = request.GET.get("month")
    selected_month = None
    display_month = None
    search_logs = []

    if year and month:
        try:
            year_int, month_int = int(year), int(month)
            selected_month = f"{year}-{int(month):02d}"
            display_month = datetime(year_int, month_int, 1).strftime('%B %Y')
            search_logs = SearchLog.objects.filter(timestamp__year=year_int, timestamp__month=month_int)
        except ValueError:
            search_logs = []

    # Group search logs into categories
    grouped_results = {}
    for log in search_logs:
        for category, obj in {
            "Property Type": log.property_type,
            "Neighborhood": log.neighborhood,
            "Price Range": log.price_search
        }.items():
            name = str(obj) if obj else "Unspecified"
            grouped_results.setdefault(category, {})
            grouped_results[category][name] = grouped_results[category].get(name, 0) + 1

    # Pass context to template
    context = {
        "month": month or "",
        "year": year or "",
        "selected_month": selected_month,
        "selected_month_label": display_month,
        "year_range": range(2025, datetime.now().year + 3),
        "months": [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ],
        "results": grouped_results,
    }

    return render(request, "reports/report.html", context)
