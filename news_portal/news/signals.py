# import os
#
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from dotenv import load_dotenv, find_dotenv
#
# from .models import PostCategory
#
# load_dotenv(find_dotenv())
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_me(sender, instance, **kwargs):
#     html_content = render_to_string(
#         'subscribe/for_subs.html',
#         {
#             'post': instance,
#             'link': f'{str(os.getenv("SITE_URL"))}/articles/{instance.pk}'
#          }
#     )
#
#     subject = f'{instance.title} on {instance.created.strftime("%Y-%m-%d")}'
#     subs = [i.subscribers.all() for i in instance.category.all()]
#     msg = EmailMultiAlternatives(
#         subject=subject,
#         body=instance.text,
#         from_email=str(os.getenv('FROM_EMAIL')),
#         to=[j.email for i in subs for j in i],
#     )
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
