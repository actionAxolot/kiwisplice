from django.contrib import admin
from models import FinancialChannel

class FinancialChannelAdmin(admin.ModelAdmin):
	pass

admin.site.register(FinancialChannel, FinancialChannelAdmin)