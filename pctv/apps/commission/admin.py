from django.contrib import admin
from models import Commission, CommissionPayment

class CommissionPaymentInline(admin.TabularInline):
    model = CommissionPayment
    extra = 0

class CommissionAdmin(admin.ModelAdmin):
    inlines = [CommissionPaymentInline,]
    

admin.site.register(Commission, CommissionAdmin)
