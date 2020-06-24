from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'code',
                    'm2', 'price', 'megler', 'sold')
    list_display_links = ('id', 'address')
    list_filter = ('sold',)
    #list_editable = ('is_published',)
    search_fields = ('code', 'address')
    list_per_page = 50


admin.site.register(Property, PropertyAdmin)
