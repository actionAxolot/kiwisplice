from django.contrib import admin
from models import FinancialInstitution, FinancialChannelClient, FinancialChannelInventory, FinancialChannelProspection


admin.site.register(FinancialInstitution)
admin.site.register(FinancialChannelClient)
admin.site.register(FinancialChannelInventory)
admin.site.register(FinancialChannelProspection)