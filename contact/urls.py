from django.urls import path
from .views import contact

urlpatterns = [
    # path('', contact_in, name='contact_in'),
    path('', contact, name='contact'),
]