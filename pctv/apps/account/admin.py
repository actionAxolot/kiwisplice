from django.contrib import admin
from models import Profile, PhoneLabel, PhoneNumber


class PhoneNumberInline(admin.TabularInline):
	model = PhoneNumber
	extra = 3


class ProfileAdmin(admin.ModelAdmin):
	exclude = ("user", )
	inlines = [
		PhoneNumberInline,
	]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(PhoneLabel)