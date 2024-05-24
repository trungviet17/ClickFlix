from django.urls import path
from . import views


app_name = "payment"

urlpatterns = [
    path("recharge/", views.recharge_account, name="recharge"),
    path("create-order/", views.create_order, name="create_order"),
    path("process/", views.payment_process, name="process"),
    path("completed/", views.payment_completed, name="completed"),
    path("canceled/", views.payment_canceled, name="canceled"),
]
