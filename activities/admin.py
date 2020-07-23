from django.contrib import admin
from activities.models import Activity, Option, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 0
    fields = ('voter',)


class OptionAdmin(admin.ModelAdmin):
    inline = [
        VoteInline
    ]
    fields = ('content', 'image')


class OptionInline(admin.TabularInline):
    model = Option
    extra = 0
    fields = ('content', 'image')


class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline
    ]
    fields = ('title', 'sponsor', 'end_datetime')


admin.site.register(Option, OptionAdmin)
admin.site.register(Activity, ActivityAdmin)
