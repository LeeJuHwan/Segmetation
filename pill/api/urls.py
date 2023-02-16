from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

app_name = "api"
# router = routers.DefaultRouter()
# router.register(r'images', views.CreateImageView)

urlpatterns = [
    # path('', views.fbv_upload, name = 'index'),
    # path('', views.CreateImageView.as_view(), name = 'index'),
    # path('', include(router.urls))
    path('',views.ImageUploadView.as_view(), name = 'index'),
    path("list/", views.ImageDetailView.as_view(), name = "img_list")
]
 
if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
