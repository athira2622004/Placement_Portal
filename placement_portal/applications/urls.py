from django.urls import path
from .views import apply_company, my_applications

urlpatterns = [
    path('apply/<int:company_id>/', apply_company, name='apply_company'),
    path('my/', my_applications, name='my_applications'),
]
