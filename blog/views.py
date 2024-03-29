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
        comment_text = request.POST['comment-text']
        user_post = Post.objects.get(sno=sl_no)

        new_comment = Comment(user=request.user, post=user_post, comment_text=comment_text)
        new_comment.save()
        messages.success(request, "Comment added successfully!!")
    else:
        messages.warning(request, "Please login to comment")

    return redirect(f'/blog/{sl_no}')


def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['textarea']
            if len(title)>5:
                if len(content)>25:
                    new_post = Post(title=title, content=content, author=request.user)
                    new_post.save()
                    messages.success(request, 'Successfully Created your post!!')
                    return redirect(f'/blog/{new_post.sno}')
                else:
                    messages.warning(request, "Please enter a valid size of content for your post...")
            else:
                messages.warning(request, "Please enter a valid size title!!")
    else:
        messages.warning(request, "Please login to write a post!!!")
    return render(request, 'blog/create_post.html')


def manage_post(request):
    if request.user.is_authenticated:
        view_user = request.user
        posts = view_user.post_set.all()
        context = {
            'posts': posts,
        }
    else:
        messages.warning(request, 'Please login to manage your post!!')
        context = {}
    return render(request, 'blog/manage_post.html', context)


def delete_post(request, sl_no):
    if request.user.is_authenticated:
        current_user = request.user
        del_post = Post.objects.get(sno=sl_no)
        if del_post.author == current_user:
            del_post.delete()
            messages.success(request, 'Post got deleted!!')
        else:
            messages.warning(request, 'You are not authorized...')
    else:
        messages.danger(request, 'Invalid Attempt!!')
    return redirect('/blog/manage_post')
    
    
