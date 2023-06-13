from django.urls import path

from blog.apps import BlogConfig

from blog import views

app_name = BlogConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts',
    ),
]
