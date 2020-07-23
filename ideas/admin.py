from django.contrib import admin
from ideas.models import Idea


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    fields = ('title', 'description', 'user', 'status')


admin.site.register(Idea, IdeaAdmin)
