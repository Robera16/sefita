from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Record

def index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})


def detail(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, 'records/detail.html',{'record': record})
    