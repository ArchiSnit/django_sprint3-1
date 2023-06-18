from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

NUM_OF_PUNBLIC = 5


def post_query():
    """Функция запроса"""
    return (
        Post.objects.select_related(
            'category',
            'location',
        )
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    )


def index(request):
    '''Функция главной страници'''
    post_list = post_query().order_by('-pub_date')[:NUM_OF_PUNBLIC]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    '''Функция отвечает за посты'''
    post = get_object_or_404(post_query(), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    '''Функция отвечает за Публикации в категории'''
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = post_query().filter(category=category)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
