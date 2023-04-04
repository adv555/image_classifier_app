from cifar_10.views import IndexView, HistoryView, show_all_images, clear_history, delete_image
from django.urls import path

app_name = 'cifar_10'

urlpatterns = [
    path('cifar10', IndexView.as_view(), name='cifar_10'),
    path('history/', HistoryView.as_view(), name='history'),
    path('history/show_all/', show_all_images, name='show_all_history'),
    path('clear_history/', clear_history, name='clear_history'),
    path('delete_image/<int:pk>/', delete_image, name='delete_image')
]