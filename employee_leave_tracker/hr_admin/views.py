from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from employee.models import LeaveRequest
from .serializers import LeaveRequestSerializer
from utils.encryption import encrypt_leave_request, decrypt_leave_request
from rest_framework.pagination import PageNumberPagination


class LeaveRequestDetailUpdateView(generics.RetrieveUpdateAPIView):
    """
    View to handle retrieval and updating of leave request details.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method to handle encryption"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        encrypted_response = encrypt_leave_request(serializer.data)
        return Response({
            "encrypted_data": encrypted_response,
            "success": True
            })
    
    def update(self, request, *args, **kwargs):
        """Handle updating a leave request where encrypted data is provided."""
        if 'encrypted_data' in request.data:
            try:
                decrypted_data = decrypt_leave_request(request.data['encrypted_data'])
            except Exception as e:
                return Response(
                    {"error": "Invalid encrypted data", "details": str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            decrypted_data = request.data

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=decrypted_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "encrypted_data": encrypt_leave_request(serializer.data),
            "success": True
        })

class LeaveRequestListView(generics.ListAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','employee_name', 'leave_type', 'start_date', 'end_date', 'status', 'reason']
    pagination_class = PageNumberPagination
    
class LeaveRequestPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10