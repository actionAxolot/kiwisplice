from django.contrib import admin
from models import FinancialChannel, ProspectionMedia, ProspectionChannel, \
	Prospection


admin.site.register(FinancialChannel)
admin.site.register(ProspectionMedia)
admin.site.register(ProspectionChannel)
admin.site.register(Prospection)