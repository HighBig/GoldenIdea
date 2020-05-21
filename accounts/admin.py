from django.contrib import admin
from accounts.models import Department, User


admin.site.register(Department)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'department')


admin.site.register(User, UserAdmin)
