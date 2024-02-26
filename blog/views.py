from django.db.models import F
from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from config.Core import CPaginator


def home_view(request):
    page = int(request.GET.get('p', 1))
    query = "SELECT * FROM blog_post WHERE is_published = true and category_id = 1 ORDER BY created_at DESC"
    posts = CPaginator(Post.objects, 6, page, query)
    d = {
        'home': 'active',
        'posts': posts,
        'categories': Category.objects.all(),
        'popular_posts': Post.objects.filter(is_published=True).order_by('-views')[:3],
        'latest_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
    }

    return render(request, 'index.html', d)


def blog_view(request):
    cat = request.GET.get('cat')
    page = int(request.GET.get('p', 1))
    search = request.GET.get('text')

    if search:
        text = search.replace('+', ' ').strip().upper()
        query = f"SELECT * FROM blog_post WHERE is_published = true and category_id = {cat} and title LIKE '%{text}%' ORDER BY created_at DESC"
        posts = CPaginator(Post.objects, 6, page, query)
    else:
        query = f"SELECT * FROM blog_post WHERE is_published = true and category_id = {cat} ORDER BY created_at DESC"
        posts = CPaginator(Post.objects, 6, page, query)

    d = {
        'posts': posts,
        'blog': 'active',
        'category': Category.objects.filter(id=cat).first,
        'search': search,
        'categories': Category.objects.all(),
        'popular_posts': Post.objects.filter(is_published=True).order_by('-views')[:3],
        'latest_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
    }

    return render(request, 'category.html', d)


def blog_detail_view(request, pk):
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post_id=pk)
    related_posts = Post.objects.filter(category=post.category, is_published=True).exclude(id=pk).order_by(
        '-created_at')[:3]

    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data.get('name'), email=data.get('email'),
                                     message=data.get('message'))
        obj.save()
        return redirect('/blog/' + str(pk))

    Post.objects.filter(id=pk).update(views=F('views') + 1)

    d = {
        'post': post,
        'popular_posts': Post.objects.filter(is_published=True).order_by('-views')[:3],
        'latest_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
        'related_posts': related_posts,
        'comments': comments,
        'blog': 'active',
        'categories': Category.objects.all()
    }

    return render(request, 'blog-single.html', d)


def about_view(request):
    page = int(request.GET.get('p', 1))
    text = "SELECT * FROM blog_post WHERE is_published = true ORDER BY created_at DESC"
    posts = CPaginator(Post.objects, 6, page, text)

    d = {
        'posts': posts,
        'about': 'active',
        'categories': Category.objects.all(),
        'popular_posts': Post.objects.filter(is_published=True).order_by('-views')[:3],
        'latest_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
    }

    return render(request, 'about.html', d)
