#  from django.shortcuts import render
#  from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, TemplateView

from .forms import FileUploadForm
from .models import FileUpload


class IndexView(TemplateView):
    template_name = 'home.html'


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'


class FileListView(ListView):
    model = FileUpload
    context_object_name = 'uploads'


class UploadFileView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    success_url = reverse_lazy('files_list')
