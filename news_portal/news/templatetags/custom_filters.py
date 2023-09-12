from django import template

register = template.Library()

bad_words = [
    'текст',
    'заголовок',
]


@register.filter()
def censor(value):
    words = value.split()
    result = []
    for word in words:
        if word in bad_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)
