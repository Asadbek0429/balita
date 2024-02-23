from django.shortcuts import render, redirect
from .models import Post, Tag, Comment


def home_view(request):
    d = {
        'home': 'active',
        'tags': Tag.objects.all()
    }
    return render(request, 'index.html', d)


def blog_view(request):
    tag = request.GET.get('tag')
    posts = Post.objects.filter(tags=tag, is_published=True).order_by('-created_at')
    d = {
        'posts': posts,
        'blog': 'active',
        'tag': Tag.objects.filter(id=tag).first,
        'tags': Tag.objects.all(),
    }
    return render(request, 'category.html', d)


def blog_detail_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post_id=pk)
    tags = []
    for tag in post.tags.all():
        tags.append(tag.id)
    related_posts = Post.objects.filter(tags=tuple(tags), is_published=True).exclude(id=pk).order_by(
        '-created_at')[:3]

    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data.get('name'), email=data.get('email'),
                                     message=data.get('message'))
        obj.save()
        return redirect('/blog/' + str(pk))

    d = {
        'post': post,
        'popular_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
        'related_posts': related_posts,
        'comments': comments,
        'blog': 'active',
        'tags': Tag.objects.all()
    }
    return render(request, 'blog-single.html', d)


def about_view(request):
    d = {
        'about': 'active',
        'tags': Tag.objects.all()
    }
    return render(request, 'about.html', d)
