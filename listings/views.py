from django.http import HttpResponse
from django.views import generic
from listings.models import listing
from django.shortcuts import get_object_or_404, render
from utils.email_sender import EmailSender
from django.views.decorators.csrf import csrf_exempt  # optional for testing only
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
import requests
from django.utils.html import escape

# def index(request):
#     return HttpResponse("Listings app")

def listings_list(request):
    listings = listing.objects.all()  # call with () to get data
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