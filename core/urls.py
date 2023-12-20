
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('login/', face_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('classify/', find_user_view, name='classify'),
    path('register', register, name='register'),
    path('signin', auth_view, name='signin'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
