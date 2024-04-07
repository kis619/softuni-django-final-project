from django.urls import path

from final_exam.threads.views import ThreadCreateView, CommentCreateView

urlpatterns = [
    path('<int:thread_id>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('<int:post_id>/', ThreadCreateView.as_view(), name='thread_create'),
]
