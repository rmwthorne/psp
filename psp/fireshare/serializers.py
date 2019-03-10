from django.conf import settings
from django.db.models import Q
from rest_framework import serializers

from .models import FileUpload


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username')


class FileUploadSerializer(serializers.ModelSerializer):
    def get_queryset(self, user):
        return FileUpload.objects.filter(
            Q(published='PU') |
            Q(user__username=self.request.user)
        )

    class Meta:
        model = FileUpload
        fields = ('name', 'url', 'created')
