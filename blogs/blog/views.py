from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, \
    DetailView, DeleteView

from .models import Follow, Post, ReadPost


class AutoFieldForUserMixin:
    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
        return super().form_valid(form)


class OnlyLoggedUserMixin:
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class NewsFeed(OnlyLoggedUserMixin, ListView):
    template_name = 'blog/index.html'
    model = Follow
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'лента новостей'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            subscriptions = self.model.objects.filter(user=self.request.user)
            return Post.objects.filter(
                user__in=[
                    subscribe.author_blog.pk for subscribe in subscriptions
                ]
            )


class ReadPosts(OnlyLoggedUserMixin, View):
    model = ReadPost

    def post(self, request, *args, **kwargs):
        post_pk = request.POST.get('read', '')
        if post_pk:
            try:
                self.model.objects.get(
                    user_id=request.user, post_id=post_pk).delete()
            except self.model.DoesNotExist:
                self.model.objects.create(
                    user_id=request.user.pk, post_id=post_pk)
        return HttpResponseRedirect(reverse_lazy('news-feed'))


class CreatePost(OnlyLoggedUserMixin, AutoFieldForUserMixin, CreateView):
    template_name = 'blog/new.html'
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'создание поста'
        return context


class UserPosts(OnlyLoggedUserMixin, ListView):
    template_name = 'blog/profile.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'мои посты'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(user=self.request.user)


class SubscribeBlog(OnlyLoggedUserMixin, CreateView):
    template_name = 'blog/subscribe_blog.html'
    model = Follow
    fields = ['author_blog']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'подписаться на блог'
        context['subscribes'] = self.get_subscribes()
        return context

    def post(self, request, *args, **kwargs):
        author_blog_pk = request.POST.get('author_blog', '')
        if author_blog_pk:
            try:
                self.model.objects.get(
                    user_id=request.user, author_blog_id=author_blog_pk
                ).delete()
            except self.model.DoesNotExist:
                self.model.objects.create(
                    user_id=request.user.pk, author_blog_id=author_blog_pk)
        return HttpResponseRedirect(reverse_lazy('subscribe-blog'))

    def get_subscribes(self):
        if self.request.user.is_authenticated:
            return self.model.objects.filter(user=self.request.user)


class UpdatePost(OnlyLoggedUserMixin, AutoFieldForUserMixin, UpdateView):
    template_name = 'blog/update_post.html'
    model = Post
    fields = ['title', 'text']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'подписаться на блог'
        return context


class DeletePost(OnlyLoggedUserMixin, AutoFieldForUserMixin, DeleteView):
    template_name = 'blog/delete_post.html'
    model = Post
    success_url = reverse_lazy('user-posts')


class PostPage(OnlyLoggedUserMixin, DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'страница поста'
        return context
