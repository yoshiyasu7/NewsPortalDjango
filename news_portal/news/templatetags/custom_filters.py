from django import template

register = template.Library()

bad_words = [
    'текст',
    'заголовок',
]

cens = lambda x: '*' * len(x)

# def cens1(w):
#     return f'{w[:1]}{"*" * (len(w) - 1)}'


@register.filter()
def censor(value):
    for bw in bad_words:
        value = value.lower().replace(bw, cens(bw))
    return value
