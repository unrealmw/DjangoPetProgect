from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Worker, Department
from .forms import WorkerForm


def index(request):
    workers = Worker.objects.all()
    departments = Department.objects.all()
    context = {"workers": workers, "departments": departments}
    return render(request, "addworker/index.html", context)


def by_department(request, department_id):
    workers = Worker.objects.filter(department=department_id)
    departments = Department.objects.all()
    current_department = Department.objects.get(pk=department_id)
    context = {'workers': workers, 'departments': departments,
               'current_department': current_department}
    return render(request, 'addworker/by_department.html', context)


class WorkerCreateView(CreateView):
    template_name = "addworker/create.html"
    form_class = WorkerForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

