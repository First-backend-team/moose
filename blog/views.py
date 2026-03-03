from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Post, Tag, About, Comment
from .form import CommentForm


def home_page(request):
    post = Post.objects.all().order_by('-id')
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)


def article_page(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'blog.html', context)


def article_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=pk)
    tag = Tag.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()


    context = {
        'posts': post,
        'tags': tag,
        'forms': form,
        'comments': comments

    }
    return render(request, 'blog-single.html', context)


def about_page(request):
    about = About.objects.all()
    context = {
        'abouts': about
    }
    return render(request, 'about.html', context)