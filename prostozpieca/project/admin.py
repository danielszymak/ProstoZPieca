from django.contrib import admin
from .models import ProportionBakings, EquipmentBaking, ProcessBakings
# Register your models here.

admin.site.register(EquipmentBaking)
admin.site.register(ProcessBakings)
admin.site.register(ProportionBakings)
