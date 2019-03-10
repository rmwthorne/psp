from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from rest_framework import routers

from psp.fireshare import views

router = routers.DefaultRouter()
router.register(
    r'files/', 
    views.FileListViewAPI.as_view(
        {'get': 'list'}
    ),
    basename='api/',
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('files/', views.FileListView.as_view(), name='files_list'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload/', views.UploadFileView.as_view(), name='upload'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
