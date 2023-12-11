from django import forms
from .models import Asset, Computer, Assignment
from authentication.models import CustomUser

class AssetCreationForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_category', 'description', 'serial_number', 'location', 'status', 'purchase_date', 'warranty_expiry_date']

    computer_id = forms.CharField(max_length=15, required=False)
    drive_serialnumber = forms.CharField(max_length=50, required=False)
    assigned_to = forms.ModelChoiceField(queryset=CustomUser.objects.all(), required=False)
    assigned_date = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['computer_id'].widget = forms.HiddenInput()
        self.fields['drive_serialnumber'].widget = forms.HiddenInput()
        self.fields['assigned_to'].widget = forms.HiddenInput()
        self.fields['assigned_date'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        asset_category = cleaned_data.get('asset_category')

        if asset_category and asset_category.name.lower() == 'computer':
            self.fields['computer_id'].required = True
            self.fields['drive_serialnumber'].required = True
        else:
            self.fields['computer_id'].required = False
            self.fields['drive_serialnumber'].required = False

        if cleaned_data.get('assign_to_user'):
            self.fields['assigned_to'].required = True
            self.fields['assigned_date'].required = True
        else:
            self.fields['assigned_to'].required = False
            self.fields['assigned_date'].required = False

        return cleaned_data

