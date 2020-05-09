from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    recent_posts = Post.objects.order_by('timeStamp')[0:3]
    context = {
        'recent_posts': recent_posts,
    }
    return render(request, 'home/home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['user-name']
        email = request.POST['user-email']
        phone = request.POST['user-phone']
        content = request.POST['user-content']

        if len(name)<2 or len(email)<7 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form correctly!!!")
        else:
            new_contact = Contact(name=name, email=email, phone=phone, content=content)
            new_contact.save()
            messages.success(request, "Details submitted successfully")
        
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['search']
    if len(query) > 50:
        posts = Post.objects.none()
        messages.warning(request, "Please enter a valid query")
    else:
        postTitle = Post.objects.filter(title__icontains=query)
        postContent = Post.objects.filter(content__icontains=query)
        posts = postTitle.union(postContent)

    if posts.count == 0:
        messages.warning(request, "Please refine your query") 

    context = {
        'posts': posts
    }
    return render(request, 'home/search.html', context)


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        if len(username)<3 or len(password1)<3 or len(password2)<3 or len(firstname)<3 or len(lastname)<3:
            messages.warning(request, "Please enter valid information!!!")
        else:
            if password1 != password2:
                messages.error(request, "Passwords did not match!!")
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully!!")
                login(request, user)
                return redirect('home')
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        user_text = request.POST['user-text']
        password = request.POST['password']

        if '@' in user_text:
            user = authenticate(request, email=user_text, password=password)
        else:
            user = authenticate(request, username=user_text, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, "Logged In Successfully")
        else:
            messages.error(request, "Invalid Credentials!!!")
    return redirect('home')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')


