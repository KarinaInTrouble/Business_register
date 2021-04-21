from django.contrib import admin

# Register your models here.
from .models import VHD, Predpriyatie, PB, PVD, Bank, BS, FO, FP, NK

admin.site.register(VHD)
admin.site.register(Predpriyatie)
admin.site.register(PB)
admin.site.register(PVD)
admin.site.register(Bank)
admin.site.register(BS)
admin.site.register(FO)
admin.site.register(FP)
admin.site.register(NK)