from django.shortcuts import render
from .forms import PostFrom
from .models import User,Post
# Create your views here.


def post_view(request):
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
