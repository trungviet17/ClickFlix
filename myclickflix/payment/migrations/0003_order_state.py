# Generated by Django 5.0.6 on 2024-05-25 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0002_rename_item_orderdetail_movie_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="state",
            field=models.CharField(
                choices=[
                    ("paying", "Paying"),
                    ("paid", "Paid"),
                    ("canceled", "Canceled"),
                ],
                default="paying",
                max_length=10,
            ),
        ),
    ]