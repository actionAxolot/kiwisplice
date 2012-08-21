from django.contrib import admin
from models import ProspectionChannel, ProspectionStatus

class ProspectionChannelAdmin(admin.ModelAdmin):
	pass


class ProspectionStatusAdmin(admin.ModelAdmin):
	"""None yet"""
	pass
		

class ClientCommentsAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(ProspectionChannel, ProspectionChannelAdmin)
admin.site.register(ProspectionStatus, ProspectionStatusAdmin)
