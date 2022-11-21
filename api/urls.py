from django.urls import path
from .view.user_view import EmployeeAPIView
from .view.admin_view import AdminAPIView
from .view.project_view import ProjectAPIView
from .view.company_view import CompanyAPIView
from .view.administrator_view import AdministratorAPIView
from .view.token_view import AdministratorTokenAPIView

urlpatterns = [
    path('administrator', AdministratorAPIView.as_view()),
    path('administrator/token', AdministratorTokenAPIView.as_view()),
    path('employee', EmployeeAPIView.as_view()),
    path('admin', AdminAPIView.as_view()),
    path('employee/project', ProjectAPIView.as_view()),
    path('company', CompanyAPIView.as_view()),
]