from django.contrib import admin

from .models import Prediction


class PredictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'property_id', 'property_adresse', 'user_id', 'user_username', 'price_prediction',
                    'actual_price')
    list_display_links = ('property_id', 'user_id')
    list_filter = ('user_id',)
    #list_editable = ('is_published',)
    search_fields = ('property_id', 'user_id')
    list_per_page = 50


admin.site.register(Prediction, PredictionAdmin)
