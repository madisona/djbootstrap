
from django.contrib import admin

from sample import models

class SampleAdmin(admin.ModelAdmin):
    list_display = ["what", "when"]
    date_hierarchy = "when"
    list_filter = ["when"]

admin.site.register(models.SampleModel, SampleAdmin)
