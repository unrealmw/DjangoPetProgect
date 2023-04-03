from django.shortcuts import render
from django.http import HttpResponse
from .models import Worker


# Create your views here.
def index(request):
    s = "Список персонала: \r\n\r\n\r\n\r"
    for worker in Worker.objects.order_by("birth_date"):
        s += f"{worker.pk} : {worker.name} {worker.last_name} {worker.patronymic} {worker.birth_date} \r\n"
    return HttpResponse(s, content_type="text/plain; charset=utf-8")
