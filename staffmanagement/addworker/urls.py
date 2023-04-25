from django.urls import path

from .views import index, by_department, WorkerCreateView

urlpatterns = [
    path('add/', WorkerCreateView.as_view(), name='add'),
    path('<int:department_id>/', by_department, name="by_department"),
    path('', index, name="index"),
]