from django.views.generic import TemplateView

from final_exam.posts.models import Post


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_at')[:3]
        return context
