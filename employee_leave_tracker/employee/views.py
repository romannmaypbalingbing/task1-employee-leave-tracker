from rest_framework import generics
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer


class LeaveRequestCreateView(generics.CreateAPIView):
    """
    View to handle creation of leave requests.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer