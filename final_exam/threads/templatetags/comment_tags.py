from django import template

register = template.Library()


@register.filter
def total_comments(post):
    return sum(thread.comment_set.count() for thread in post.thread_set.all())
