from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from final_exam.accounts.views import SignUpView, LutLoginView, LutLogoutView, ProfileDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LutLoginView.as_view(), name='login'),
    path('logout/', LutLogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='accounts/registration/password_change.html'),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'),
         name='password_change_done'),

    path('profile/', ProfileDetailView.as_view(), name='profile_detail'),
]
