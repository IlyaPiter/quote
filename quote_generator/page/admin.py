from django.contrib import admin

from .models import Masterpiece, Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'source',
        'value',
        'views',
        'likes',
        'dislikes'
    )
    list_editable = (
        'source',
        'value'
    )
    search_fields = ('content',)
    list_filter = ('source',)
    list_display_links = ('content',)


class MasterpieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_editable = ('author',)
    search_fields = ('title',)
    list_filter = ('author',)
    list_display_links = ('title',)


admin.site.register(Quote, QuoteAdmin)
admin.site.register(Masterpiece, MasterpieceAdmin)
