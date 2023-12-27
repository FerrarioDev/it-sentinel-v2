from django import forms
from .models import Asset


class AssetCreationForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_number', 'asset_category', 'description', 'serial_number', 'location', 'status', 'purchase_date', 'warranty_expiry_date']
