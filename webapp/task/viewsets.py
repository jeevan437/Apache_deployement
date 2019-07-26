from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmpSerializer

class EmpViewSet(ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmpSerializer