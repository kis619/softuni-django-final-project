from django.urls import path

from final_exam.posts.views import PostListView, PostCreateView, PostDetailView, PostDeleteView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:post_id>/comment/', CommentCreateView.as_view(), name='comment_create'),

]
