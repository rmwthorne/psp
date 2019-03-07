from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import FileUpload
from .forms import FileUploadForm


class FileListView(ListView):
    model = FileUpload
    context_object_name = 'uploads'


class UploadFileView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    success_url = reverse_lazy('files_list')
