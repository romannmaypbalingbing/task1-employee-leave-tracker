# from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from employee.models import LeaveRequest
from .serializers import LeaveRequestSerializer

class LeaveRequestDetailUpdateView(generics.RetrieveUpdateAPIView):
    """
    View to handle retrieval and updating of leave request details.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    lookup_field = 'id'

class LeaveRequestListView(generics.ListAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','employee_name', 'leave_type', 'start_date', 'end_date', 'status', 'reason']