from django.urls import path
from .views import insert_employee, retrieve_employees

urlpatterns = [
    path('insert_employee/', insert_employee, name='insert_employee'),
    path('retrieve_employees/', retrieve_employees, name='retrieve_employees'),
]
