from django.urls import path

from final_exam.reactions.views import ReactionCreateView

urlpatterns = [
    path('post/<int:post_id>/', ReactionCreateView.as_view(), name='post_react'),
    path('comment/<int:comment_id>/', ReactionCreateView.as_view(), name='comment_react'),
]