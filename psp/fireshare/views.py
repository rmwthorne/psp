from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, TemplateView

from .forms import FileUploadForm
from .models import FileUpload


class IndexView(TemplateView):
    template_name = 'home.html'


class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('index')


class FileListView(ListView):
    model = FileUpload
    context_object_name = 'uploads'


class UploadFileView(CreateView):
    model = FileUpload
    form_class = FileUploadForm
    success_url = reverse_lazy('index') # change this
    #  success_url = reverse_lazy('files_list')
    template_name = 'upload.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(UploadFileView, self).form_valid(form)
