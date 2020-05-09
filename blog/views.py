from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def blog_view(request):
    allPost = Post.objects.all()
    context = {
        'allPost': allPost
    }
    return render(request, 'blog/blog_view.html', context)


def blogPost(request, sl_no):
    if request.user.is_authenticated:
        post = Post.objects.get(sno=sl_no)
        context = {
            'post': post,
        }
        return render(request, 'blog/blogPost.html', context)
    else:
        messages.warning(request, 'Please login to view in details!!!')
        return redirect('blog_view')
