# Generated by Django 4.2 on 2023-06-02 17:06

import autoslug.fields
import dirtyfields.dirtyfields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('name',), verbose_name='This is domain')),
                ('domain', models.CharField(blank=True, help_text='By default, it will use SLUG as domain. But if you have a domain, you can write down your domain here instance using SLUG.', max_length=100, unique=True)),
                ('kind', models.CharField(blank=True, db_index=True, max_length=40)),
                ('tax_number', models.CharField(blank=True, max_length=255)),
                ('registration_no', models.CharField(blank=True, max_length=50)),
                ('website_url', models.URLField(blank=True)),
                ('blog_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('summary', models.CharField(blank=True, help_text='Short summary about company.', max_length=1000)),
                ('description', models.CharField(blank=True, help_text='Longer description about company.', max_length=1000)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PLACEHOLDER', 'Placeholder'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('HIDDEN', 'Hidden'), ('REMOVED', 'Removed')], db_index=True, default='DRAFT', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discount_offset', models.SmallIntegerField(default=0, help_text='We accept only percent here. For product, we will update the final price of a product regarding this percent.')),
                ('role', models.CharField(choices=[('STAFF', 'Staff'), ('ADMIN', 'Admin'), ('OWNER', 'Owner'), ('CUSTOMER', 'Customer'), ('DELIVERER', 'Deliverer')], max_length=20)),
                ('status', models.CharField(choices=[('INVITED', 'Invited'), ('PENDING', 'Pending'), ('ACTIVE', 'Active'), ('SUSPEND', 'Suspend'), ('REJECTED', 'Rejected'), ('DEACTIVATE', 'Deactivate'), ('HIDDEN', 'Hidden'), ('REMOVED', 'Removed')], default='PENDING', max_length=20)),
                ('is_default', models.BooleanField(default=False)),
            ],
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TransactionOrganizationUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_number', models.PositiveIntegerField(blank=True, editable=False, unique=True)),
                ('total_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payable_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.CharField(blank=True, max_length=700)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
