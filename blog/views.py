from django.shortcuts import render, HttpResponse, redirect
from .models import Post, Comment
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def blog_view(request):
    allPost = Post.objects.all()
    context = {
        'allPost': allPost,
    }
    return render(request, 'blog/blog_view.html', context)


def blogPost(request, sl_no):
    if request.user.is_authenticated:
        post = Post.objects.get(sno=sl_no)
        comments = Comment.objects.filter(post=post)
        context = {
            'post': post,
            'comments': comments
        }
        return render(request, 'blog/blogPost.html', context)
    else:
        messages.warning(request, 'Please login to view in details!!!')
        return redirect('blog_view')


def user_comment(request, sl_no):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            comment_text = request.POST['comment']
            user_post = Post.objects.filter(sno=sl_no)
            
            new_comment = Comment(user=user, comment_text=comment_text, post=user_post)
            new_comment.save()
            messages.success(request, "Comment added successfully!!")
    else:
        messages.warning(request, 'Please login to comment!!!')
    
    return redirect(f'/blog/{sl_no}')
    
    
