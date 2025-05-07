from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils.html import escape
from listings.models import listing, property_type, neighborhood, price_search, SearchLog
from utils.email_sender import EmailSender
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def listings_list(request):
    logger.info("test")
    listings = listing.objects.filter(is_visible=True) #displays only the listings with the visible box checked

    # Filters from dropdowns
    price_range = request.GET.get('price_range')
    property_type_id = request.GET.get('property_type')
    neighborhood_name = request.GET.get('neighborhood')

    # Keep track of objects for logging
    selected_property_type = None
    selected_neighborhood = None
    selected_price_range = None

    #listings = listing.objects.all()

    if property_type_id and property_type_id.isdigit():
        selected_property_type = property_type.objects.filter(pk=property_type_id).first()
        if selected_property_type:
            listings = listings.filter(property_type=selected_property_type)

    if neighborhood_name:
        selected_neighborhood = neighborhood.objects.filter(neighborhood_name=neighborhood_name).first()
        if selected_neighborhood:
            listings = listings.filter(neighborhood=selected_neighborhood)
        else:
            listings = listings.none()

    if price_range and price_range.isdigit():
        selected_price_range = price_search.objects.filter(pk=price_range).first()
        if selected_price_range:
            min_price = selected_price_range.min_price
            max_price = selected_price_range.max_price
            if max_price == 0:
                listings = listings.filter(property_price__gte=min_price)
            else:
                listings = listings.filter(property_price__gte=min_price, property_price__lte=max_price)
        else:
            listings = listings.none()

    # Create a SearchLog if any filters were applied
    if selected_property_type or selected_neighborhood or selected_price_range:
        SearchLog.objects.create(
            property_type=selected_property_type,
            neighborhood=selected_neighborhood,
            price_search=selected_price_range,
        )

    context = {
        'listings': listings,
        'property_types': property_type.objects.all(),
        'neighborhoods': neighborhood.objects.all(),
        'price_ranges': price_search.objects.all().order_by('min_price'),
    }

    return render(request, 'listings/listings.html', context)


def details(request, listing_id):
    listingItem = get_object_or_404(listing, pk=listing_id)
    return render(request, "listings/details.html", {"listingItem": listingItem})


def send_test_email(request):
    name = request.POST.get('name')
    sender_email = request.POST.get('sender_email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    listing_info = request.POST.get('listing_info')

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

    try:
        response = EmailSender.send_email(
            to_email="ckRealEstateOmaha@gmail.com",
            subject="Test Email",
            text_body="This is a test email sent via Mailgun.",
            html_body=html_body,
        )

        # If successful, add a success message
        messages.success(request, "Email sent successfully")

    except Exception as e:
        messages.error(request, "Email failed to send")


    return HttpResponse("Email sent successfully!")


def search_listings(request):

    logger.info("test2")
    property_type_id = request.GET.get('property_type')
    neighborhood_id = request.GET.get('neighborhood')
    price_search_id = request.GET.get('price_search')

    listings = listing.objects.all()

    if property_type_id:
        listings = listings.filter(property_type_id=property_type_id)
    if neighborhood_id:
        listings = listings.filter(neighborhood__name=neighborhood_id)
    if price_search_id:
        listings = listings.filter(price_search_id=price_search_id)

    # Log the search
    logger.info("checking if we need a log for search")
    if property_type_id or neighborhood_id or price_search_id:
        logger.info("yep, creating one")
        SearchLog.objects.create(
            property_type_id=property_type_id or None,
            neighborhood_id=neighborhood_id or None,
            price_search_id=price_search_id or None,
        )
    else:
        logger.info("nope, thats a big no dog")

    context = {
        'listings': listings,
        'property_types': property_type.objects.all(),
        'neighborhoods': neighborhood.objects.all(),
        'price_ranges': price_search.objects.all(),
    }
    return render(request, 'listings/search_results.html', context)