# Generated by Django 4.2.4 on 2023-09-21 08:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "notificationio",
            "0002_notificationuserpreference_enable_cart_notification_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="notificationuserreceiver",
            unique_together={("notification", "user")},
        ),
    ]