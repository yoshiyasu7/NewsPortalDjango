from django.urls import path
from django.views.decorators.cache import cache_page
from .views import (
    NewsList, NewsDetail, ArticlesList,
    ArticlesDetail, PostList, PostSearch,
    NewsCreate, NewsUpdate, NewsDelete,
    ArticlesCreate, ArticlesUpdate, ArticlesDelete,
    CategoryListView, subscribe
)

urlpatterns = [
    path('posts/', cache_page(60)(PostList.as_view()), name='post_list'),
    path('posts/search/', PostSearch.as_view(), name='post_search'),
    path('news/', cache_page(60*5)(NewsList.as_view()), name='news_list'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('news/create', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit', NewsUpdate.as_view(), name='news_edit'),
    path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
    path('articles/', cache_page(60*5)(ArticlesList.as_view()), name='articles_list'),
    path('articles/<int:pk>', ArticlesDetail.as_view(), name='articles_detail'),
    path('articles/create', ArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit', ArticlesUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete', ArticlesDelete.as_view(), name='articles_delete'),
    path('category/<int:pk>', cache_page(60*5)(CategoryListView.as_view()), name='categories'),
    path('category/<int:pk>/subscribe', subscribe, name='subscribe'),
]

