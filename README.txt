"""
Команды запускаемые в Django shell.
"""

# 1. Создать двух пользователей
# (с помощью метода User.objects.create_user('username')).
from news_portal.news.models import *

u1 = User.objects.create_user('Тюлень534')
u2 = User.objects.create_user('Медведь210')

# 2. Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(user=u1)
Author.objects.create(user=u2)

# 3. Добавить 4 категории в модель Category.
с1 = Category.objects.create('Экономика')
с2 = Category.objects.create('Спорт')
с3 = Category.objects.create('Политика')
с4 = Category.objects.create('Культура')

# 4. Добавить 2 статьи и 1 новость.
a1 = Author.objects.get(pk=1)
a2 = Author.objects.get(pk=2)

ar1 = Post.objects.create(post_type=Post.article,
                          title='Заголовок статьи 1.',
                          text='Текст статьи 1 про спорт и культуру.',
                          author=a1)
ar2 = Post.objects.create(post_type=Post.article,
                          title='Заголовок статьи 2.',
                          text='Текст статьи 2 про экономику.',
                          author=a2)
n1 = Post.objects.create(title='Заголовок новости 1.',
                         text='Текст новости 1 про политику.',
                         author=a2)

# 5. Присвоить им категории
# (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategory.objects.create(post=ar1, category=c2)
PostCategory.objects.create(post=ar1, category=c4)
PostCategory.objects.create(post=ar2, category=c1)
PostCategory.objects.create(post=n1, category=c3)

# 6. Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).
ar1 = Post.objects.get(pk=1)
ar2 = Post.objects.get(pk=2)
n1 = Post.objects.get(pk=3)

Comment.objects.create(post=ar1, user=a2, text='Комментарий к статье 1')
Comment.objects.create(post=ar1, user=a1, text='Ответный комментарий к статье 1')
Comment.objects.create(post=ar2, user=a1, text='Комментарий к статье 2')
Comment.objects.create(post=n1, user=a2, text='Комментарий к статье 3')

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям,
# скорректировать рейтинги этих объектов.
ar1.like()
ar1.like()
ar1.like()
ar1.dislike()
ar2.like()
ar2.dislike()
n1.like()
n1.dislike()
n1.dislike()

comm1 = Comment.objects.get(pk=1)
comm2 = Comment.objects.get(pk=2)
comm3 = Comment.objects.get(pk=3)
comm4 = Comment.objects.get(pk=4)

comm1.like()
comm1.dislike()
comm1.like()
comm2.like()
comm3.like()
comm3.like()
comm3.dislike()
comm3.dislike()
comm4.like()
comm4.like()
comm4.like()
comm4.like()
comm4.like()
comm4.dislike()

# 8. Обновить рейтинги пользователей.
a1.update_rating()
a2.update_rating()

# 9. Вывести username и рейтинг лучшего пользователя
# (применяя сортировку и возвращая поля первого объекта).
best_user = Author.objects.order_by('-author_rating').values('user__username', 'author_rating').first()
print(f"Лучший пользователь: {best_user['user__username']}, его рейтинг: {best_user['author_rating']}")

# 10. Вывести дату добавления, username автора, рейтинг,
# заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
best_article = Post.objects.filter(post_type='AR').order_by('-post_rating').first()
print("Лучшая статья:", best_article.created.strftime('%d.%m.%Y %H:%M:%S'),
      best_article.author.user.username, best_article.title,
      best_article.preview(), sep='\n')

# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
comments = Comment.objects.filter(post=best_article)
for c in comments:
    print(f"дата: {c.created.strftime('%d.%m.%Y %H:%M:%S')}, пользователь: {c.user.username}\n"
          f"рейтинг {c.comment_rating}, текст комментария: {c.text}")
