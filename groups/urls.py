from django.urls import path
from .views import GroupCreateView, GroupDetailView, GroupUpdateView, GroupDeleteView
from . import views

urlpatterns = [
    path('groups/', views.Groups, name='groups-home'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group/new/', GroupCreateView.as_view(), name='group-create'),
    path('group/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('group/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),

]