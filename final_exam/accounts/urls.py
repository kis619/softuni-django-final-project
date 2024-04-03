from django.urls import path

from final_exam.accounts.views import SignUpView, LutLoginView, LutLogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LutLoginView.as_view(), name='login'),
    path('logout/', LutLogoutView.as_view(), name='logout'),

]
