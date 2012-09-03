from django.contrib import admin
from models import ProspectionMedia, ProspectionChannel, \
	Prospection, PhoneNumber, PhoneLabel

class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	fk_name = "prospection"


class ProspectionAdmin(admin.ModelAdmin):
	list_display = (
		'salesperson',
		'visitation_date',
		'status',
	)

	list_filter = (
		'salesperson',
		'visitation_date',
		'status',
	)

	inlines = (
		PhoneNumberInline,
	)


admin.site.register(ProspectionMedia)
admin.site.register(ProspectionChannel)
admin.site.register(PhoneNumber)
admin.site.register(PhoneLabel)
admin.site.register(Prospection, ProspectionAdmin)