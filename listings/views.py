from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils.html import escape
from listings.models import listing, property_type, neighborhood, price_search, SearchLog
from utils.email_sender import EmailSender
from django.contrib import messages


def listings_list(request):
    listings = listing.objects.filter(is_visible=True) #displays only the listings with the visible box checked

    # Filters from dropdowns
    price_range = request.GET.get('price_range')
    property_type_id = request.GET.get('property_type')
    neighborhood_name = request.GET.get('neighborhood')

    #listings = listing.objects.all()

    if property_type_id and property_type_id.isdigit():
        listings = listings.filter(property_type_id=int(property_type_id))

    if neighborhood_name:
        try:
            neighborhood_obj = neighborhood.objects.get(neighborhood_name=neighborhood_name)
            listings = listings.filter(neighborhood=neighborhood_obj)
        except neighborhood.DoesNotExist:
            listings = listings.none()

    if price_range and price_range.isdigit():
        try:
            price_obj = price_search.objects.get(pk=price_range)
            min_price = price_obj.min_price
            max_price = price_obj.max_price

            if max_price == 0:  # You can treat max=0 as open-ended
                listings = listings.filter(property_price__gte=min_price)
            else:
                listings = listings.filter(property_price__gte=min_price, property_price__lte=max_price)

        except price_search.DoesNotExist:
            listings = listings.none()

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
    if property_type_id or neighborhood_id or price_search_id:
        SearchLog.objects.create(
            property_type_id=property_type_id or None,
            neighborhood_id=neighborhood_id or None,
            price_search_id=price_search_id or None,
        )

    context = {
        'listings': listings,
        'property_types': property_type.objects.all(),
        'neighborhoods': neighborhood.objects.all(),
        'price_ranges': price_search.objects.all(),
    }
    return render(request, 'listings/search_results.html', context)