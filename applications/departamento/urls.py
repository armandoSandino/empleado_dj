from django.contrib import admin
from django.urls import path
from .views import NewRegisterDepartmentView

app_name = 'department_app'

urlpatterns = [
    path('new-department/', NewRegisterDepartmentView.as_view(), name='new-depart')
]