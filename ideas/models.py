from django.db import models
from common.models import BaseModel


class Idea(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
