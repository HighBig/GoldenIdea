from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField("last modified datetime", blank=True)

    def save(self, *args, **kwargs):
        if not kwargs.pop('skip_modified_datetime', False):
            self.modified_datetime = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
