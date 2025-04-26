from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import get_object_or_404, render
from utils.email_sender import send_email
from django.views.decorators.csrf import csrf_exempt  # optional for testing only
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.all()  # call with () to get data
    return render(request, 'listings/listings.html', {'listings': listings})


def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})

@require_POST
def send_test_email(request):
    context = {
        'subject': "This is a test email",
        'body': 'We are trying to reach you about your car’s extended warranty',
    }
    try:
        send_email(context)
        return JsonResponse({'message': 'Email sent successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'message': 'Failed to send email'}, status=500)