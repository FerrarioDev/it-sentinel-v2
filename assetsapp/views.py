from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from .forms import AssetCreationForm
from .models import Asset, Computer, Assignment


@login_required(login_url='/auth/login')
def index(request):
    return render(request, 'assetsapp/index.html')


class Add_assets(View):
    @csrf_exempt
    def get(self, request):
        form = AssetCreationForm(initial={'asset_number': '', 'description': '', 'serial_number': '', 'location': '', 'purchase_date': '', 'warranty_expiry_date': ''})
        return render(request, 'assetsapp/add_asset.html', {'form': form})
    
    @csrf_exempt
    def post(self, request):
        form = AssetCreationForm(request.POST)
        if form.is_valid():
            asset_id = form.cleaned_data['asset_number']
            category = form.cleaned_data['asset_category']
            serial_number = form.cleaned_data['serial_number']
            
            if Asset.objects.filter(asset_number = asset_id).exists():
                messages.error(request, 'Asset ID is already registered')
                return render(request, 'assetsapp/add_asset.html', {'form': form})
    
            if Asset.objects.filter(serial_number=serial_number).exists():
                messages.error(request, 'Serial Number is already registered')
                return render(request, 'assetsapp/add_asset.html', {'form': form})
            
            computer_id = "Z20012" + asset_id
            
            asset = form.save(commit=False)

            # Optionally create a Computer object
            if category.name == 'Computer':
                computer = Computer(computer_id = computer_id, asset=asset)
                computer.save()
                asset.computer = computer  # Associate the Computer object with the Asset

            asset.save()

            # Redirect to the asset_detail view
            return redirect('asset_list')
            # return redirect('asset_detail', asset_number=asset.asset_number)

        # If the form is invalid, render the form page with errors
        print(form.errors)
        return render(request, 'assetsapp/add_asset.html', {'form': form})

class AssetListView(ListView):
    model = Asset
    template_name = 'assetsapp/dashboard.html'
    context_object_name = 'assets'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
