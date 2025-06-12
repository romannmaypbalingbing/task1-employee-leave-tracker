from django.urls import path
from .views import LeaveRequestCreateView

urlpatterns = [
    path('leave-request/', LeaveRequestCreateView.as_view(), name='leave-request-create'),
]
