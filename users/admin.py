from django.contrib import admin

from users.models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "id"]
    search_fields = ["username",]
    sortable_by = ("username",)
    list_filter = ("username",)   # this is stupidity cause username is unique ;)

    # and you can write manually function and customize admin panel

