from django.contrib import admin
from .models import Mission,Category,Location


admin.site.register(Category)
admin.site.register(Location)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):

    list_display = ["title","detail","startDate","budget"]

    list_display_links = ["title","startDate"]

    search_fields= ["title"]

    list_filter = ["startDate"]

    class Meta:
        model=Mission

