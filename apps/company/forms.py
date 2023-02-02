from django import forms

# Local
from company.models import (
    Pen,
    Quantity
)


class PenForm(forms.ModelForm):
    """Pen form."""

    class Meta:
        model = Pen
        exclude = ('datetime_deleted',)
        fields = '__all__'


class QuantityForm(forms.ModelForm):
    """Quantityform."""

    class Meta:
        model = Quantity
        fields = '__all__'
