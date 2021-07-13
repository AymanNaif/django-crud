from django.urls import path
from .views import HomeView, SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snack-list', SnackListView.as_view(), name='snack-list'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack-detail'),
    path('snack-create', SnackCreateView.as_view(), name='snack-create'),
    path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack-update'),
    path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack-delete'),

]
