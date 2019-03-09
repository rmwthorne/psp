from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


class FileUpload(models.Model):
    PRIVATE = 'PR'
    PUBLIC = 'PU'
    PUBLISH_CHOICES = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    )

    name = models.CharField(max_length=100)
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            )
    upload = models.FileField(upload_to='files/')
    published = models.CharField(max_length=2, choices=PUBLISH_CHOICES, default=PRIVATE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name
