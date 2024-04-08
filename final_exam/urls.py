from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
        [
            path('admin/', admin.site.urls),
            path('', include('final_exam.home.urls')),
            path('accounts/', include('final_exam.accounts.urls')),
            path('posts/', include('final_exam.posts.urls')),
            path('conversations/', include('final_exam.threads.urls')),  # threads
            path('reactions/', include('final_exam.reactions.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
