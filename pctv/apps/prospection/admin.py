from django.contrib import admin
from models import Prospection, PhoneNumber, PhoneLabel

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

	exclude = (
		'salesperson',
	)

	inlines = (
		PhoneNumberInline,
	)

	def save_model(self, request, obj, form, change):
		obj.salesperson = request.user
		obj.save()


admin.site.register(PhoneNumber)
admin.site.register(PhoneLabel)
admin.site.register(Prospection, ProspectionAdmin)