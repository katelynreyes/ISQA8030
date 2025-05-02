from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import get_object_or_404, render
from django.contrib.humanize.templatetags.humanize import intcomma
from utils.email_sender import EmailSender
from django.views.decorators.csrf import csrf_exempt  # optional for testing only
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
import requests
from django.utils.html import escape
from listings.models import SearchLog, property_type, neighborhood, price_search

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.filter(is_visible=True)
    for listing_item in listings:
        # Get the first photo for each listing
        listing_item.first_photo = listing_item.listing_photo_set.first()
    return render(request, 'listings/listings.html', {'listings': listings})


def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})

def send_test_email(request):
    print(request.POST)
    # Example email content
    name = request.POST.get('name')
    sender_email = request.POST.get('sender_email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    listing_info = request.POST.get('listing_info')  # This is your autofilled field
    recipient_email = request.POST.get('email')  # The hidden email input

    to_email = "ckRealEstateOmaha@gmail.com"
    subject = "Test Email"
    text_body = "This is a test email sent via Mailgun."
    # html_body = "<p>This is a <strong>test email</strong> sent via Mailgun.</p>"

    html_body = f"""
    <h1>New Request Received</h1><br/>
    <ul>
        <li><strong>Name:</strong> {escape(name)}</li>
        <li><strong>Email:</strong> {escape(sender_email)}</li>
        <li><strong>Phone:</strong> {escape(phone)}</li>
        <li><strong>Message:</strong> {escape(message)}</li>
        <li><strong>Regarding:</strong> {escape(listing_info)}</li>
    </ul>
    """

    # Sending the email
    response = EmailSender.send_email(
        to_email=to_email,
        subject=subject,
        text_body=text_body,
        html_body=html_body,
    )

    return HttpResponse("Email sent successfully!")

    # if response and response.status_code == 200:
    #     return HttpResponse("Email sent successfully!")
    # else:
    #     return HttpResponse(f"Failed to send email: {response.status_code if response else 'No response'}")

def search_listings(request):
    property_type_id = request.GET.get('property_type')
    neighborhood_id = request.GET.get('neighborhood')
    price_search_id = request.GET.get('price_search')

    listings = listing.objects.all()

    if property_type_id:
        listings = listings.filter(property_type_id=property_type_id)
    if neighborhood_id:
        listings = listings.filter(neighborhood_id=neighborhood_id)
    if price_search_id:
        listings = listings.filter(price_search_id=price_search_id)

    # Log the search
    if property_type_id or neighborhood_id or price_search_id:
        SearchLog.objects.create(
            property_type_id=property_type_id if property_type_id else None,
            neighborhood_id=neighborhood_id if neighborhood_id else None,
            price_search_id=price_search_id if price_search_id else None
        )

    context = {
        'listings': listings,
        'property_types': property_type.objects.all(),
        'neighborhoods': neighborhood.objects.all(),
        'price_ranges': price_search.objects.all(),
    }

    return render(request, 'listings/search_results.html', context)