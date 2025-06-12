from rest_framework import serializers
from employee.models import LeaveRequest

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        read_only_fields = ['id', 'employee_name', 'leave_type', 'start_date', 'end_date', 'reason', 'created_at']
