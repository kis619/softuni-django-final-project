from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from final_exam.accounts.forms import LetUsTalkUserCreationForm, LetUsTalkUserLoginForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = LetUsTalkUserCreationForm
    success_url = reverse_lazy('login')


class LutLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LetUsTalkUserLoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')


class LutLogoutView(LogoutView):
    pass


class ProfileDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.letustalkuserprofile  # TODO figure out whether to override the method
