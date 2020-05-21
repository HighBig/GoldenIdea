from django.contrib import admin
from ideas.models import Idea


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Idea, IdeaAdmin)
