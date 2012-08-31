from django.contrib import admin
from models import FinancialChannel, ProspectionMedia, ProspectionChannel, \
	Prospection
from apps.account.models import Profile


class ProspectionAdmin(admin.ModelAdmin):
	pass


admin.site.register(FinancialChannel)
admin.site.register(ProspectionMedia)
admin.site.register(ProspectionChannel)
admin.site.register(Prospection, ProspectionAdmin)