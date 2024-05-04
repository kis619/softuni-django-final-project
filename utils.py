from django.db.models import Count

from final_exam.reactions.models import Reaction
from final_exam.threads.models import Comment, Thread


def get_post_id_from_comment_id(comment_id):
    comment = Comment.objects.get(pk=comment_id)
    thread_id = comment.thread_id
    post_id = get_post_id_from_thread_id(thread_id)
    return post_id


def get_post_id_from_thread_id(thread_id):
    thread = Thread.objects.get(pk=thread_id)
    post_id = thread.post_id
    return post_id


def add_reactions_to_threads(threads, user):
    for thread in threads:
        comments = thread.comment_set.all()
        for comment in comments:
            comment_reactions = Reaction.objects.filter(comment=comment, users=user).values_list(
                'reaction_type', flat=True)
            comment.user_reactions = {reaction: True for reaction in comment_reactions}

            comment_reactions = Reaction.objects.filter(comment=comment).values('reaction_type').annotate(
                count=Count('id'))
            comment.reactions_count = {reaction['reaction_type']: reaction['count'] for reaction in
                                       comment_reactions}
        thread.comments = comments
