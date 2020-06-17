from django.db import models
from common.models import BaseModel


class Idea(BaseModel):
    STATUSES = (
        (0, '未采纳'),
        (1, '已采纳')
    )

    title = models.CharField(max_length=256)
    description = models.TextField()
    status = models.IntegerField(default=0, choices=STATUSES)
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='user'
    )
    acceptor = models.ForeignKey(
        'accounts.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='acceptor'
    )
    accept_datetime = models.DateTimeField(blank=True, null=True)

    @property
    def is_accepted(self):
        return self.status == 1

    def __str__(self):
        return self.title
