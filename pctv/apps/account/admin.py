from django.contrib import admin
from models import Profile, ClientComments

class ProfileAdmin(admin.ModelAdmin):
	pass

class ClientCommentsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(ClientComments, ClientCommentsAdmin)
