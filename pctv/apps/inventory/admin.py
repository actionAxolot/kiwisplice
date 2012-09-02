from django.contrib import admin
from models import Prototype, Section, Inventory, \
	BridgeCredit, BridgeCreditPayment, UtilityType, UtilityPayment


admin.site.register(Prototype)
admin.site.register(Section)
admin.site.register(Inventory)
admin.site.register(BridgeCredit)
admin.site.register(BridgeCreditPayment)
admin.site.register(UtilityType)
admin.site.register(UtilityPayment)