
from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Quote, Masterpiece

# ...и регистрируем её в админке:
admin.site.register(Quote)
admin.site.register(Masterpiece)