from django.urls import path

from final_exam.posts.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list'),
]
