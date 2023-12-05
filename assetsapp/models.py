from django.db import models
from authentication.models import CustomUser

STATUS = (
    ('USE','Use'),
    ('DISUSE','disuse'),
    ('IDLE', 'idle'),
    )

class AssetCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    asset_number = models.CharField(primary_key=True, max_length=9, unique=True)
    asset_category = models.ForeignKey('AssetCategory', on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True)
    serial_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=50)
    status = models.CharField(max_length=9, choices = STATUS, default="USE")
    purchase_date = models.DateField()
    warranty_expiry_date = models.DateField()

    def __str__(self):
        return f"{self.asset_category.name} - {self.serial_number}"

class Computer(models.Model):
    computer_id = models.CharField(primary_key=True, max_length=15, unique=True)
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE)
    drive_serialnumber = models.CharField(max_length=50)    


    def __str__(self):
        return f"Computer ID: {self.computer_id} - Asset: {self.asset}"


class Assignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.asset} assigned to {self.assigned_to}"
