from django.urls import path
from .views import home_view, blog_view, blog_detail_view, about_view

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('blog/<int:pk>/', blog_detail_view),
    path('about/', about_view),
]
