from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
