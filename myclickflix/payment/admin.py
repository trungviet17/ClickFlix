from django.contrib import admin
from .models import OrderDetail, RechargeCode, Order

# Register your models here.


@admin.register(RechargeCode)
class RechargeCodeAdmin(admin.ModelAdmin):
    list_display = ["code", "amount", "quantity"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["profile", "total_amount", "state", "created_at"]
