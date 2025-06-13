from rest_framework import generics, status
from rest_framework.response import Response
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer
from utils.encryption import encrypt_leave_request, decrypt_leave_request

class LeaveRequestCreateView(generics.CreateAPIView):
    """
    View to handle creation of leave requests.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

    def create(self, request, *args, **kwargs):
        """Override create method to handle encryption"""

        #check if incoming data is encrypted
        if 'encrypted_data' in request.data:
            try:
                decrypted_data = decrypt_leave_request(request.data['encrypted_data'])
            except Exception as e:
                return Response(
                    {"error":"Invalid encrypted data", "details":str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            decrypted_data = request.data
        
        serializer = self.get_serializer(data=decrypted_data)
        serializer.is_valid(raise_exception=True)
        leave_request = serializer.save()

        response_data = {
            "id": str(leave_request.id),
            "employee_name": leave_request.employee_name,
            "leave_type": leave_request.leave_type,
            "start_date": leave_request.start_date.isoformat(),
            "end_date": leave_request.end_date.isoformat(),
            "status": leave_request.status,
            "message": "Leave request submitted successfully"
        }

        encrypted_response= encrypt_leave_request(response_data)

        return Response(
            {
                "encrypted_data": encrypted_response,
                "success": True
            },
            status=status.HTTP_201_CREATED
        )