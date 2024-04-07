from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from final_exam.accounts.forms import LetUsTalkUserCreationForm, LetUsTalkUserLoginForm, LetUsTalkUserProfileForm

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
        return self.request.user.letustalkuserprofile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserModel
    form_class = LetUsTalkUserProfileForm
    template_name = 'accounts/profile_update.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user.letustalkuserprofile

    def get_success_url(self):
        return reverse_lazy('profile_detail')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
