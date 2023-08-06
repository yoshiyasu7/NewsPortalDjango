import django_filters as df
from django import forms
from .models import *


class PostFilter(df.FilterSet):
    title = df.CharFilter(lookup_expr='icontains',
                          label='Заголовок',
                          widget=forms.TextInput(attrs={'placeholder': 'Поиск по названию'})
                          )
    author = df.ModelChoiceFilter(empty_label='Все авторы',
                                  label='Авторы',
                                  queryset=Author.objects.all()
                                  )
    category = df.ModelChoiceFilter(empty_label='Все категории',
                                    label='Категория',
                                    queryset=Category.objects.all()
                                    )
    created = df.DateFilter(lookup_expr='gte',
                            label='Дата',
                            widget=forms.DateInput(attrs={'type': 'date'})
                            )

    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'created', ]
