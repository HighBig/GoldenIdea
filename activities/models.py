from django.db import models
from django.db.models import Count, Max
from django.utils import timezone
from common.models import BaseModel
from common.debug_utils import debug


class Activity(BaseModel):
    STATUSES = (
        (0, '进行中'),
        (1, '已结束')
    )

    title = models.CharField(max_length=256)
    sponsor = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )
    end_datetime = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(default=0, choices=STATUSES)

    @property
    def is_finished(self):
        return self.status == 1 or timezone.now() > self.end_datetime

    @property
    def option_max_vote_num(self):
        return self.option_set \
                   .all() \
                   .annotate(vote_num=Count('vote')) \
                   .aggregate(Max('vote_num'))['vote_num__max']

    @property
    def voted_users(self):
        return Vote.objects \
                   .filter(option__in=self.option_set.all()) \
                   .values_list('voter', flat=True)

    def get_ordered_options(self):
        return self.option_set \
                   .all() \
                   .annotate(vote_num=Count('vote')) \
                   .order_by('-vote_num')

    def __str__(self):
        return self.title


class Option(BaseModel):
    activity = models.ForeignKey(
        'activities.Activity',
        on_delete=models.CASCADE,
    )
    content = models.CharField(
        blank=True,
        null=True,
        max_length=256
    )
    image = models.FileField(
        blank=True,
        null=True,
        upload_to='options/%Y/%m/%d'
    )

    @property
    def is_won(self):
        debug(self.activity.option_max_vote_num)
        return self.vote_set.count() == self.activity.option_max_vote_num

    def get_voters(self):
        return self.vote_set.all().values_list('voter', flat=True)

    def __str__(self):
        return self.content


class Vote(BaseModel):
    option = models.ForeignKey(
        'activities.Option',
        on_delete=models.CASCADE,
    )
    voter = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.option.content + ' ' + self.voter.username
