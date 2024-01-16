# Generated by Django 4.2.4 on 2023-08-14 12:25

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):
    dependencies = [
        ("accountio", "0003_alter_organizationuser_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="contact_number",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="organization",
            name="height",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="imo_number",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="organization",
            name="ppoi",
            field=versatileimagefield.fields.PPOIField(
                default="0.5x0.5", editable=False, max_length=20
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="store_front_photo",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                height_field="height",
                null=True,
                upload_to="",
                width_field="width",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="organization",
            name="width",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]