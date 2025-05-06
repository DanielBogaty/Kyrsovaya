from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import AddPostForm, AddCommentForm
from core.utils import DataMixin
import fcalmaz.settings as settings


class ForumHome(DataMixin, ListView):
    template_name = 'forum/home.html'
    context_object_name = 'posts'
    title_page = 'Главная страница форума'

    def get_queryset(self):
        return Post.published.all().order_by('-time_update')
    

class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'forum/addpost.html'
    title_page = 'Написать пост'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)
    

class ShowPost(DataMixin, DetailView):
    template_name = 'forum/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset = None):
        return get_object_or_404(Post.objects.all(), slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('time_create')
        context['form_class'] = AddCommentForm()
        context['default_image'] = settings.DEFAULT_USER_IMAGE
        return self.get_mixin_context(context, title=context['post'].title)
    

class AddComment(LoginRequiredMixin, View):
    def post(self, request, post_slug):
        post = get_object_or_404(Post.published, slug=post_slug)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        return redirect('forum:post', post_slug=post.slug)
