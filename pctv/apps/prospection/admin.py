from django.contrib import admin
from models import ProspectionMedia, ProspectionChannel, \
	Prospection

class ProspectionAdmin(admin.ModelAdmin):
	list_display = (
		'salesperson',
		'prospect',
		'visitation_date',
		'status',
	)

	list_filter = (
		'salesperson',
		'prospect',
		'visitation_date',
		'status',
	)


admin.site.register(ProspectionMedia)
admin.site.register(ProspectionChannel)
admin.site.register(Prospection, ProspectionAdmin)