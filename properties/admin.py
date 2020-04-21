from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'adresse', 'finnkode',
                    'primarareal', 'prisantydning', 'megler', 'solgt')
    list_display_links = ('id', 'adresse')
    list_filter = ('solgt',)
    #list_editable = ('is_published',)
    search_fields = ('finnkode', 'adresse')
    list_per_page = 50


admin.site.register(Property, PropertyAdmin)
