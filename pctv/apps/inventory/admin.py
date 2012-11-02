from django.contrib import admin
from models import Prototype, Section, Inventory, \
    BridgeCredit, BridgeCreditPayment, Condo


class InventoryAdmin(admin.ModelAdmin):
    readonly_fields = ('cuv',)


admin.site.register(Prototype)
admin.site.register(Section)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(BridgeCredit)
admin.site.register(BridgeCreditPayment)
admin.site.register(Condo)
