from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AssetCreationForm
from .models import Asset, Computer, Assignment

@login_required(login_url='/auth/login')
def index(request):
    return render(request, 'assetsapp/index.html')

def add_assets(request):
    if request.method == 'POST':
        form = AssetCreationForm(request.POST)
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

            # return redirect('asset_detail', asset_number=asset.asset_number)
            return render(request, 'assetsapp/add_asset.html', {'form': form})
    else:
        form = AssetCreationForm()

    return render(request, 'assetsapp/add_asset.html', {'form': form})
