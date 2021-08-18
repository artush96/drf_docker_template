from django.core.mail import EmailMessage


def send_mail(subject, body, to_mail):
    email = EmailMessage('subject', 'body', to=['to_mail'])
    email.send()
