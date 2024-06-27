from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload_image'),  # Example upload URL
    path('success/', views.upload_success, name='upload_success'),  # Example success URL
    path('', views.home, name='home'),  # Root URL pattern mapped to home view
    path('predictions/', views.predictions, name='predictions'),
    path('create_report/', views.create_report, name='create_report'),
    # path('report/<int:report_id>/', views.view_report, name='view_report'),
    path('reports/', views.list_reports, name='list_reports'),
]

# Serve uploaded files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve uploaded files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)