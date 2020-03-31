from django.contrib import admin

from .models import Prediction


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'user', 'price_prediction',
                    'actual_price')
    list_display_links = ('property_id', 'user')
    list_filter = ('user',)
    #list_editable = ('is_published',)
    search_fields = ('property_id', 'user')
    list_per_page = 50


admin.site.register(Prediction, PredictionAdmin)
