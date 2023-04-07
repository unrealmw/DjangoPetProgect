from django.shortcuts import render


from .models import Worker


def index(request):
    workers = Worker.objects.all()
    context = {"workers": workers}
    return render(request, "addworker/index.html", context)

