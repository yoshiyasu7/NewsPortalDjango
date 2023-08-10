import os
import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from celery import shared_task

from dotenv import load_dotenv, find_dotenv

from .models import Post, Category

load_dotenv(find_dotenv())


@shared_task
def notify_me(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = f'{post.created.strftime("%Y-%m-%d")} {post.title}'
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for user in subscribers_users:
            subscribers_emails.append(user.email)

    html_content = render_to_string(
        'subscribe/for_subs.html',
        {
            'post': post,
            'link': f'{str(os.getenv("SITE_URL"))}/articles/{pk}'
         }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=str(os.getenv('FROM_EMAIL')),
        to=subscribers_emails,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print('Уведомление отправлено.')


@shared_task
def week_news():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(created__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'week_posts.html',
        {
            'link': str(os.getenv('SITE_URL')),
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=str(os.getenv('FROM_EMAIL')),
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print('Еженедельная рассылка отправлена.')
