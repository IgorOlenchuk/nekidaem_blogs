from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from .forms import PostForm
from .models import Post, Follow

User = get_user_model()


#@cache_page(60 * 1440)
def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context ={
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'index.html', context, content_type='text/html', status=200)


@login_required
def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(
                        request.POST,
                        files=request.FILES or None,
        )
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    labels = {
        'title': "Добавить запись",
        'button': "Добавить",
    }
    return render(request, 'new.html', {'form': form, 'labels': labels})


def profile(request, username):
    profile = get_object_or_404(get_user_model(), username=username)
    post_list = profile.author_posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    following = get_object_or_404(User, username=username)
    context = {
        'profile': profile,
        'page': page,
        'paginator': paginator,
        'following': following,
    }
    return render(request, 'profile.html', context)


def post_view(request, username, post_id):
    profile = get_object_or_404(get_user_model(), username=username)
    post = get_object_or_404(Post, id=post_id, author__username=username)
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'profile': profile,
        'post': post,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'post.html', context)


@login_required
def follow_index(request):
    post_list = Post.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'paginator': paginator,
    }
    return render(request, "follow.html", context)


@login_required
def profile_follow(request, username):
    follower = request.user
    following = get_object_or_404(User, username=username)
    follows = Follow.objects.filter(user=follower, author=following)
    if follows.exists() or follower.username == following.username:
        return redirect("profile", username=username)
    Follow.objects.create(user=follower, author=following)
    return redirect("profile", username=username)


@login_required
def profile_unfollow(request, username):
    my_user = request.user
    profile = get_object_or_404(User, username=username)
    subscription = Follow.objects.filter(user=my_user, author=profile)
    if subscription.exists():
        subscription.delete()
    return redirect("profile", username=request.user.username)
