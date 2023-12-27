from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from .forms import AssetCreationForm
from .models import Asset, Computer, Assignment
import csv

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
            
            computer_id = "Z20012" + str(asset_id)
            
            asset = form.save(commit=False)
            asset.save()
            # Optionally create a Computer object
            if category.name == 'Computer':
                computer = Computer(computer_id = computer_id, asset=asset)
                computer.save()
                asset.computer = computer  # Associate the Computer object with the Asset

            # Redirect to the asset_detail view
            return redirect('asset_list')
            # return redirect('asset_detail', asset_number=asset.asset_number)

        # If the form is invalid, render the form page with errors
        return render(request, 'assetsapp/add_asset.html', {'form': form})

class AssetListView(ListView):
    model = Asset
    template_name = 'assetsapp/dashboard.html'
    context_object_name = 'assets'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
def Upload_from_csv(request):
    file_path = "assetsapp/Inventario_Hardware_Dnar_10-2023.csv"

    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)  # Read the header row

        # Assuming your CSV file has 6 columns, modify the range accordingly
        for row in csv_reader:
            if len(row) == 6:
                # Access individual columns using indices (0-based)
                col1 = row[0]
                col2 = row[1]
                col3 = row[2]
                col4 = row[3]
                col5 = row[4]
                col6 = row[5]   

                print(f"Column 1: {col1}, Column 2: {col2}, ..., Column 6: {col6}")
    
    # You can pass the CSV data to the template for rendering if needed
    return redirect('asst_list')