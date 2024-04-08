from django.urls import reverse
from django.views.generic.edit import CreateView

from utils import get_post_id_from_comment_id
from .models import Reaction


class ReactionCreateView(CreateView):
    model = Reaction
    fields = ['reaction_type']
    template_name = 'posts/post_detail.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get('post_id')
        form.instance.comment_id = self.kwargs.get('comment_id')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        post_id = self.kwargs.get('post_id')

        if post_id is None:
            post_id = get_post_id_from_comment_id(self.kwargs.get('comment_id'))
        return reverse('post_detail', args=[post_id])
