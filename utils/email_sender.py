import time
import requests
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailSender:
    MAILGUN_API_KEY = settings.MAILGUN_API_KEY
    MAILGUN_DOMAIN = settings.MAILGUN_DOMAIN

    @classmethod
    def send_email(cls, to_email, subject, text_body, html_body=None, from_email=None, retries=3, delay=3):
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

        for attempt in range(retries):
            try:
                response = requests.post(url, auth=auth, data=data)

                if response.status_code == 200:
                    logger.info(f"Email successfully sent to {to_email}")
                    return response
                else:
                    logger.warning(
                        f"Attempt {attempt + 1} failed to send email to {to_email}. Status: {response.status_code}. Retrying...")

            except requests.RequestException as e:
                logger.error(f"Exception while sending email to {to_email}: {str(e)}")

            # Wait before retrying
            time.sleep(delay * (attempt + 1))  # Exponential backoff

        logger.error(f"Failed to send email to {to_email} after {retries} attempts.")
        return None