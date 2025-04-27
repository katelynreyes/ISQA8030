# from django.template.loader import render_to_string
# from django.core.mail import EmailMessage

# def send_email(context):
#     subject = context.get('subject')
#     html_message = render_to_string('email_template.html', context)
#     to_email = 'ckRealEstateOmaha@gmail.com'
#     to_email = [to_email]
#     from_email = 'ckrealestateomaha@gmail.com'
#     message = EmailMessage(subject=subject, body=html_message, from_email=from_email, to=to_email)
#     message.content_subtype = 'html'
#     message.send()


# def send_email(to_email, subject, text_body, html_body=None):
#     MAILGUN_API_KEY = 'f66d45e2c9ddcce3685a3d4596ad6caa-10b6f382-23fc4ec2'
#     MAILGUN_DOMAIN = 'sandboxfb0fd4584db04eda90dba7052cd77d91.mailgun.org'  # e.g., 'mg.yourdomain.com'
#
#     url = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages"
#     auth = ("api", MAILGUN_API_KEY)
#
#     data = {
#         "from": f"Your Name <mailgun@{MAILGUN_DOMAIN}>",
#         "to": [to_email],
#         "subject": subject,
#         "text": text_body,
#     }
#
#     if html_body:
#         data["html"] = html_body
#
#     response = requests.post(url, auth=auth, data=data)
#
#     return response



import requests
import logging

from django.conf import settings

logger = logging.getLogger(__name__)

class EmailSender:
    MAILGUN_API_KEY = settings.MAILGUN_API_KEY
    MAILGUN_DOMAIN = settings.MAILGUN_DOMAIN

    @classmethod
    def send_email(cls, to_email, subject, text_body, html_body=None, from_email=None):
        if not cls.MAILGUN_API_KEY or not cls.MAILGUN_DOMAIN:
            logger.error("Mailgun API key or domain not configured.")
            return None

        url = f"https://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages"
        auth = ("api", cls.MAILGUN_API_KEY)

        from_address = from_email or f"Your Name <mailgun@{cls.MAILGUN_DOMAIN}>"

        data = {
            "from": from_address,
            "to": [to_email],
            "subject": subject,
            "text": text_body,
        }

        if html_body:
            data["html"] = html_body

        try:
            response = requests.post(url, auth=auth, data=data)
            if response.status_code == 200:
                logger.info(f"Email successfully sent to {to_email}")
            else:
                logger.error(f"Failed to send email to {to_email}: {response.status_code} {response.text}")
            return response
        except requests.RequestException as e:
            logger.exception(f"Exception while sending email to {to_email}: {str(e)}")
            return None