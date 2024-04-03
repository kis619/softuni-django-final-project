from django.urls import path

from final_exam.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
