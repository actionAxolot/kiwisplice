from django.contrib import admin
from models import Profile, PhoneLabel, PhoneNumber
from apps.prospection.models import Prospection


class ProspectionInline(admin.TabularInline):
	model = Prospection
	fk_name = "prospect"
	extra = 1
	max_num = 1


class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	extra = 3


class ProfileAdmin(admin.ModelAdmin):
	exclude = ("user", )
	inlines = [
		ProspectionInline,
		PhoneNumberInline,
	]


admin.site.register(Profile, ProfileAdmin)