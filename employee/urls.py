
from django.urls import path
from employee.api import EmployeeApi,EmployeeCreateApi,EmployeeUpdateApi,EmployeeDeleteApi

urlpatterns = [
    path('api/create',EmployeeCreateApi.as_view()),
    path('api/',EmployeeApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/<int:pk>/delete',EmployeeUpdateApi.as_view()),

]
