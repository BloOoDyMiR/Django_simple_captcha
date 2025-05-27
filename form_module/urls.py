from django.urls import path
from .views import contact_view, homeView

urlpatterns = [
    path('contact', contact_view, name='contact'),
    path('', homeView.as_view(), name='home'),
]
