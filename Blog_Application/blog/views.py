from django.shortcuts import render
from .forms import PostFrom
from .models import User,Post
# Create your views here.


def add_post(request):
    template_name = 'blog/post.html'
    form = PostFrom()
    if request.method == 'POST':
        form = PostFrom(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,template_name,context)


def home_view(request):
    template_name = 'blog/home.html'
    all_posts = Post.objects.all().order_by('-posted_at')
    context={'all_posts':all_posts}
    return render(request,template_name,context)


def blog_details(request,pk):
    template_name = 'blog/blog_details.html'
    blog_post =  Post.objects.get(id=pk)
    context={'blog_post':blog_post}
    return render(request,template_name,context)


