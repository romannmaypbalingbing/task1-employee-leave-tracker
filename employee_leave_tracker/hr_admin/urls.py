from django.urls import path
from .views import LeaveRequestListView, LeaveRequestDetailUpdateView

urlpatterns = [
    path('leave-requests/', LeaveRequestListView.as_view(), name='leave-request-list'),
    path('leave-requests/<str:id>/', LeaveRequestDetailUpdateView.as_view(), name='leave-request-detail'),
]

