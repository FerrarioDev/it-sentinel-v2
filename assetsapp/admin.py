from django.contrib import admin
from .models import Asset, Assignment, Computer, AssetCategory
# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetCategory)
admin.site.register(Computer)
admin.site.register(Assignment)