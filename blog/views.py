from django.shortcuts import render, HttpResponse
from .models import Post, BlogComment
from django.contrib.auth.decorators import login_required

# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    context = {
        'allPost': allPost
    }
    return render(request, 'blog/blogHome.html', context)


def blogPost(request, sl_no):
    post = Post.objects.get(sno=sl_no)
    comments = BlogComment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/blogPost.html', context)


def blogComment(request):
    if request.method == "POST":
        pass

    return redirect("/")