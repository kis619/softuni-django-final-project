from django.db.models import Count
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from .form import PostForm
from .models import Post
from ..reactions.models import Reaction


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post_reactions = Reaction.objects.filter(post=post).values('reaction_type').annotate(count=Count('id'))
        context['post_reactions_count'] = {reaction['reaction_type']: reaction['count'] for reaction in post_reactions}

        if self.request.user.is_authenticated:
            user_reactions = Reaction.objects.filter(post=post, users=self.request.user).values_list('reaction_type',
                                                                                                     flat=True)
            context['user_reactions'] = {reaction: True for reaction in user_reactions}

            threads = post.thread_set.all()
            for thread in threads:
                comments = thread.comment_set.all()
                for comment in comments:
                    comment_reactions = Reaction.objects.filter(comment=comment, users=self.request.user).values_list(
                        'reaction_type', flat=True)
                    comment.user_reactions = {reaction: True for reaction in comment_reactions}

                    comment_reactions = Reaction.objects.filter(comment=comment).values('reaction_type').annotate(
                        count=Count('id'))
                    comment.reactions_count = {reaction['reaction_type']: reaction['count'] for reaction in
                                               comment_reactions}
                thread.comments = comments
            context['threads'] = threads
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs.update({'files': self.request.FILES})
        return kwargs


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('posts_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            return HttpResponseForbidden()
        return super().delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
