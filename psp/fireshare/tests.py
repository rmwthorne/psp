from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from psp.fireshare import views


class TestViews(TestCase):
    def test_root_url_resolves_to_index_view(self):
        resolved = resolve('/')
        self.assertEqual(resolved.func.view_class, views.IndexView)

    def test_login_url_resolves_to_user_login_view(self):
        resolved = resolve('/login/')
        self.assertEqual(resolved.func.view_class, LoginView)

    def test_files_url_resolves_to_file_list_view(self):
        resolved = resolve('/files/')
        self.assertEqual(resolved.func.view_class, views.FileListView)

    def test_upload_url_resolves_to_upload_form_view(self):
        resolved = resolve('/upload/')
        self.assertEqual(resolved.func.view_class, views.UploadFileView)
