from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created')


class NewsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'all_news.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(post_type='NE')
        return queryset.order_by('-created')


class NewsDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', )

    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NE'
        return super().form_valid(form)


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', )

    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )

    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class PostSearch(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-created'
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 10

    # Функция получения списка публикаций
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'all_articles.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().filter(post_type='AR')
        return queryset.order_by('-created')


class ArticlesDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'article.html'
    context_object_name = 'post'


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post', )

    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AR'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post', )

    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post', )

    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('articles_list')

