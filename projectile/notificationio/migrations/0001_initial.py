# Generated by Django 4.2.4 on 2023-09-19 09:09

import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orderio', '0007_historicalreturnorderproduct_historicalorderdelivery_and_more'),
        ('accountio', '0008_historicaltransactionorganizationuser_and_more'),
        ('catalogio', '0010_merge_20230919_1457'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('changed_data', models.JSONField(default=dict, help_text='Will save the previous data using serializer')),
                ('is_success', models.BooleanField(help_text='If response status is below than 400, it will save as success response')),
                ('message', models.CharField(blank=True, help_text='Message for notification if needed', max_length=500)),
                ('action_type', models.CharField(choices=[('READ', 'Read'), ('ADDITION', 'Addition'), ('CHANGE', 'Change'), ('DELETION', 'Deletion'), ('LOGIN', 'Login'), ('LOGOUT', 'Logout')], help_text='Requested method', max_length=10)),
                ('model_type', models.CharField(choices=[('USER', 'User'), ('ORGANIZATION', 'Organization'), ('ORGANIZATION_USER', 'Organization User'), ('PRODUCT', 'Product'), ('ORDER', 'Order'), ('ORDER_DELIVERY', 'Order Delivery')], max_length=30)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountio.organization')),
            ],
            options={
                'ordering': ('-created_at',),
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NotificationUserReceiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=False)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notificationio.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NotificationModelConnector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='notificationio.notification')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orderio.order')),
                ('order_delivery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orderio.orderdelivery')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountio.organization')),
                ('organization_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountio.organizationuser')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogio.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NotificationUserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enable_user_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('enable_product_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('enable_order_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('enable_order_delivery_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('enable_organization_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('enable_organization_user_notification', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off'), ('OFF BY ADMIN', 'Off by admin')], default='ON', max_length=15)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accountio.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'organization')},
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
