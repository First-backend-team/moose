from django.urls import path
from .views import home_page, article_page, article_detail, about_page

urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', article_page, name='blog'),
    path('blog/<int:pk>/', article_detail, name='detail'),
    path('about/', about_page, name='about'),
]
