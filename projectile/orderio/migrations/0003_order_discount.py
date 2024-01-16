# Generated by Django 4.2.2 on 2023-06-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orderio", "0002_returnorderproduct_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="discount",
            field=models.DecimalField(
                decimal_places=2,
                default=0,
                help_text="This is discount will appy on order total price, only accept percentage.",
                max_digits=10,
            ),
        ),
    ]
