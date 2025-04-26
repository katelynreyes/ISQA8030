from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def send_email(context):
    subject = context.get('subject')
    html_message = render_to_string('email_template.html', context)
    to_email = 'ckRealEstateOmaha@gmail.com'
    to_email = [to_email]
    from_email = 'noreply@mailjet.com'
    message = EmailMessage(subject=subject, body=html_message, from_email=from_email, to=to_email)
    message.content_subtype = 'html'
    message.send()
