from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Record, PostImage

def index(request):
    if (request.user.is_authenticated):
        records = Record.objects.all()
        return render(request, 'records/index.html', {'records': records})
    else:
        raise Http404("Unauthorized")

def detail(request, record_id):
    if (request.user.is_authenticated):
        record = get_object_or_404(Record, pk=record_id)
        photos = PostImage.objects.filter(record=record)
        return render(request, 'records/detail.html',{'record': record, 'photos':photos})
    else:
        raise Http404("Unauthorized")