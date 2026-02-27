from django.urls import path
from .views import home_page, article_page
urlpatterns = [
    path('', home_page, name='home'),
    path('blog/', article_page, name='blog'),

]