from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        auth_p_rating = Post.objects.filter(author_id=self.pk).\
            aggregate(r1=Coalesce(Sum('post_rating'), 0))
        auth_c_rating = Comment.objects.filter(user_id=self.user).\
            aggregate(r2=Coalesce(Sum('comment_rating'), 0))
        auth_p_c_rating = Comment.objects.filter(post__author__user=self.user).\
            aggregate(r3=Coalesce(Sum('comment_rating'), 0))

        self.author_rating = auth_p_rating * 3 + auth_c_rating + auth_p_c_rating
        self.save()


class Category(models.Model):
    name = models.CharField(unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NE'

    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новости')
    ]

    post_type = models.CharField(max_length=2, choices=POSITIONS, default=news)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    post_rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def preview(self):
        return f'{self.text[:123]}...' if len(str(self.text)) > 124 else f'{self.text}'

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()
