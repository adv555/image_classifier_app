from cifar_10.views import IndexView, ProfileView
from django.urls import path

app_name = 'cifar_10'

urlpatterns = [
    path('cifar10', IndexView.as_view(), name='cifar_10'),
    path('history/', ProfileView.as_view(), name='history'),
]