from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from utils.email_sender import EmailSender

def about(request):
    return render(request, 'contact/aboutus.html')

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