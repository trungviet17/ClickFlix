from django.urls import path
from . import views


app_name = "payment"

urlpatterns = [
    path("recharge/", views.recharge_account, name="recharge"),
    path("process/<int:order_id>", views.payment_process, name="process"),
    path("completed/<int:order_id>", views.payment_completed, name="completed"),
    path("canceled/<int:order_id>", views.payment_canceled, name="canceled"),
    path(
        "delete-order-detail/<int:orderdetail_id>/",
        views.delete_order_detail,
        name="delete_order_detail",
    ),
    path("delete-order/<int:order_id>/", views.delete_order, name="delete_order"),
    path("history/", views.order_history, name="order_history"),
    path("create_order/", views.create_order, name="create_order"),
    path("order_detail/<int:order_id>/", views.order_detail, name="order_detail"),
]
