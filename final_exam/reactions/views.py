from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView

from utils import get_post_id_from_comment_id
from .models import Reaction


class ReactionCreateView(CreateView):
    model = Reaction
    fields = ['reaction_type']
    template_name = 'posts/post_detail.html'

    def form_valid(self, form):
        reaction = form.instance
        user = self.request.user
        reaction.post_id = self.kwargs.get('post_id')
        reaction.comment_id = self.kwargs.get('comment_id')
        existing_reaction = Reaction.objects.filter(
            reaction_type=reaction.reaction_type,
            users=user,
            post_id=reaction.post_id,
            comment_id=reaction.comment_id
        ).first()

        if existing_reaction:
            existing_reaction.users.remove(user)
            if not existing_reaction.users.exists():
                existing_reaction.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            reaction.save()
            reaction.users.add(user)
        return super().form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs.get('post_id') or get_post_id_from_comment_id(self.kwargs.get('comment_id'))
        return reverse('post_detail', args=[post_id])


#TODO: not refresh when reacting to a thread??
# TODO: add a reaction count for comments