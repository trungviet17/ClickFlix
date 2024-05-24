from django.contrib import admin
from .models import OrderDetail, RechargeCode

# Register your models here.


@admin.register(RechargeCode)
class RechargeCodeAdmin(admin.ModelAdmin):
    list_display = ["code", "amount", "quantity"]
