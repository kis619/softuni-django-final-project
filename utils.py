from final_exam.threads.models import Comment, Thread


def get_post_id_from_comment_id(comment_id):
    comment = Comment.objects.get(pk=comment_id)
    thread_id = comment.thread_id
    thread = Thread.objects.get(pk=thread_id)
    post_id = thread.post_id
    return post_id
