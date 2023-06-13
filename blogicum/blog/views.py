from blog.models import Category, Post
from django.shortcuts import get_object_or_404, render
from django.utils import timezone


def index(request):
    '''Функция главной страници'''
    post_list = Post.objects.select_related(
        'location'
        ).filter(is_published=True,
                 category__is_published=True,
                 pub_date__lt=timezone.now()
                 ).order_by('title')[0:5]
    context = {
        'post_list': post_list
        }
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lt=timezone.now()
        ), pk=post_id
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    '''Функция отвечает за Публикации в категории'''
    category_slug = get_object_or_404(
         Category.objects.exclude(
            'title',
            'description',
         ).filter(slug=category_slug,
                  is_published=True
                  )
    )
    context = {
        'category_slug': category_slug,
    }
    return render(request, 'blog/category.html', context)
