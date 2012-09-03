from django.contrib import admin
from models import Prototype, Section, Inventory, \
	BridgeCredit, BridgeCreditPayment, UtilityType, UtilityPayment


class InventoryAdmin(admin.ModelAdmin):
	readonly_fields = ('unique_id',)


admin.site.register(Prototype)
admin.site.register(Section)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(BridgeCredit)
admin.site.register(BridgeCreditPayment)
admin.site.register(UtilityType)
admin.site.register(UtilityPayment)