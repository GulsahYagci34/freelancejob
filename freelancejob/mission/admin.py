from django.contrib import admin
from .models import Mission,Location,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_fields = {'slug':('name',)}


class LocationAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Mission)

