from django import forms
from django.core.exceptions import ValidationError

from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('content', 'source', 'value')

    def clean(self):
        super().clean()
        if self.cleaned_data:
            if self.cleaned_data['source'].masterpieces.count() >= 3:
                raise ValidationError(
                    'У одного источника не должно быть больше трех цитат')
