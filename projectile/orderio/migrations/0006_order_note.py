# Generated by Django 4.2.4 on 2023-09-14 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orderio", "0005_returnorderproduct_is_return_by_merchant"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="note",
            field=models.TextField(blank=True),
        ),
    ]
