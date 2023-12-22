from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View
from .forms import AssetCreationForm
from .models import Asset, Computer, Assignment


@login_required(login_url='/auth/login')
def index(request):
    return render(request, 'assetsapp/index.html')

class Add_assets(View):
    
    def get(self, request):
        form = AssetCreationForm(initial={'asset_number': '', 'description': '', 'serial_number': '', 'location': '', 'purchase_date': '', 'warranty_expiry_date': ''})
        return render(request, 'assetsapp/add_asset.html', {'form': form})

    def post(self, request):
        form = AssetCreationForm(request.POST, initial={'asset_number': '', 'description': '', 'serial_number': '', 'location': '', 'purchase_date': '', 'warranty_expiry_date': ''})
        if form.is_valid():
            asset = form.save(commit=False)

            # Optionally create a Computer object
            if form.cleaned_data.get('is_computer'):
                computer = Computer(computer_id=form.cleaned_data['computer_id'], drive_serialnumber=form.cleaned_data['drive_serialnumber'])
                computer.save()
                asset.computer = computer  # Associate the Computer object with the Asset

            asset.save()

            # Optionally create an Assignment object
            if form.cleaned_data.get('assign_to_user'):
                assignment = Assignment(asset=asset, assigned_to=form.cleaned_data['assigned_to'], assigned_date=form.cleaned_data['assigned_date'])
                assignment.save()

            # Redirect to the asset_detail view
            return redirect('asset_detail', asset_number=asset.asset_number)

        # If the form is invalid, render the form page with errors
        print('not created')
        return render(request, 'assetsapp/add_asset.html', {'form': form})
