from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from companies.models import Company
from .models import Application

@login_required
def apply_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    Application.objects.get_or_create(
        student=request.user,
        company=company
    )
    return redirect('my_applications')

@login_required
def my_applications(request):
    applications = Application.objects.filter(student=request.user)
    return render(request, 'student/my_applications.html', {
        'applications': applications
    })
