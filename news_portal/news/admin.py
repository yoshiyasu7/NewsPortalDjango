from django.contrib import admin
from .models import Author, Post, Category, Comment, PostCategory


# # функция Обнуления рейтинга поста
def nullfy_rating(modeladmin, request, queryset):
    queryset.update(post_rating=0)


nullfy_rating.short_description = 'Обнулить рейтинг поста'


# создаём класс для представления постов в админке
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'post_type', 'post_rating')
    list_filter = ('title', 'created', 'post_type', 'post_rating')
    search_fields = ('title', 'category__name')
    actions = [nullfy_rating]


# Register your models here.

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)
