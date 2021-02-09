from django.contrib import admin
from .models import Bakings, ProportionBaking, EquipmentBaking, ProcessBaking
# Register your models here.

admin.site.register(Bakings)
admin.site.register(ProportionBaking)
admin.site.register(ProcessBaking)
admin.site.register(EquipmentBaking)


