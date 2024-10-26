from django.urls import path
from .views import department_report_view

urlpatterns = [
    path('report/department/', department_report_view, name='department_report'),
]
