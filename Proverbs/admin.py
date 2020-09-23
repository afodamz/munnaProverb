from django.contrib import admin
from .models import *


# Register your models here.
class ProverbsAdmin(admin.ModelAdmin):
    list_display = ['content', 'date_created', 'date_modified']
    list_display_links = ['content']
    list_filter = ['date_created']
    search_fields = ['content', 'category', 'ethnic']


admin.site.register(Ethnic)
admin.site.register(Interpretation)
admin.site.register(Translation)
admin.site.register(Proverb, ProverbsAdmin)