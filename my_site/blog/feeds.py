import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog'

    def items(self):
        # Извлекает включаемые в новостную ленту объекты.
        return Post.published.all()[:5]

    def item_title(self, item):
        # Получают возвращаемый метод items() объект и возвращает заголовок
        return item.title

    def item_description(self, item):
        # Получают возвращаемый метод items() объект и возвращает описание
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        # Получают возвращаемый метод items() объект и возвращает дату
        return item.publish

