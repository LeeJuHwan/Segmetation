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
    path("detail/", views.detail_fbv, name = "detail"),
    path('cam/',views.ImageUploadView.as_view(), name = 'find_image'),
    path("list/<int:pk>", views.ImageDetailView.as_view(), name = "img_list"),
    path("search/", views.Search.as_view(), name = "search_word"),
    path("", views.TabView.as_view(), name = "index"),
    # path("search_result", views.search_result, name="search_result")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

