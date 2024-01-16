# Generated by Django 4.2.5 on 2023-10-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountio', '0011_alter_transactionorganizationuser_options'),
        ('notificationio', '0004_alter_notificationmodelconnector_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationmodelconnector',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountio.transactionorganizationuser'),
        ),
        migrations.AddField(
            model_name='notificationuserpreference',
            name='enable_transaction_notification',
            field=models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15),
        ),
        migrations.AlterField(
            model_name='notification',
            name='model_type',
            field=models.CharField(choices=[('USER', 'User'), ('ORGANIZATION', 'Organization'), ('ORGANIZATION_USER', 'Organization User'), ('PRODUCT', 'Product'), ('ORDER', 'Order'), ('ORDER_DELIVERY', 'Order Delivery'), ('CART', 'Cart'), ('CART_PRODUCT', 'Cart Product'), ('TRANSACTION', 'Transaction')], max_length=30),
        ),
    ]
