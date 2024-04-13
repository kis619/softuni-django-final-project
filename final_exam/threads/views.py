from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from utils import add_reactions_to_threads, get_post_id_from_thread_id
from .models import Thread, Comment
from ..posts.models import Post


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        response = super().form_valid(form)
        Comment.objects.create(
            author=self.request.user,
            thread=self.object,
            content=form.instance.content,
        )
        return response

    def form_invalid(self, form):
        post = Post.objects.get(pk=self.kwargs['post_id'])
        threads = post.thread_set.all()
        add_reactions_to_threads(threads, self.request.user)
        return render(
            self.request,
            template_name='posts/post_detail.html',
            context={
                'errors': form.errors,
                'post': post,
                'threads': threads,
            })

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['post_id']})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def dispatch(self, request, *args, **kwargs):
        self.thread = Thread.objects.get(pk=self.kwargs['thread_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thread = self.thread
        return super().form_valid(form)

    def form_invalid(self, form):
        post_id = get_post_id_from_thread_id(self.kwargs['thread_id'])
        post = Post.objects.get(pk=post_id)

        threads = post.thread_set.all()
        add_reactions_to_threads(threads, self.request.user)
        return render(
            self.request,
            template_name='posts/post_detail.html',
            context={
                'errors': form.errors,
                'post': post,
                'threads': threads,
            })

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.thread.post_id})
