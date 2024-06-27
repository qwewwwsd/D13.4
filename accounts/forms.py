from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives
from django.core.mail import mail_admins


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        subject='Добро пожаловать в наш новостной портал!',
        text=f'{user.username}, вы успешно зарегистрировались!',
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/products">сайте</a>!'
        )
        
        msg = EmailMultiAlternatives(
            subject=subject, body=None, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )
        
        return user