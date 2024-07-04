import datetime

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import User, NewsPost, Category
import time


@shared_task
def send_mail_new_post(pk):
    post = NewsPost.objects.get(id=pk)
    categories = post.category.all()

    emails = User.objects.filter(
        subscriptions__category=categories
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории {categories}'

    text_content = (
        f'Пост: {post.title}\n'
        f'Текст: {post.text}\n\n'
        f'Ссылка на товар: http://127.0.0.1:8000{post.get_absolute_url()}'
    )
    html_content = (
        f'Пост: {post.title}<br>'
        f'Текст: {post.text}'
        f'<a href="http://127.0.0.1:8000{post.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )
    
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@shared_task()
def weekly_send_emails():
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    posts = NewsPost.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))

    html_content = render_to_string(
        'weekly_post.html',
        {
            'link': 'http://127.0.0.1:8000',
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body=None,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()