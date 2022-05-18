# Generated by Django 4.0.4 on 2022-05-18 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sales_contact', models.ForeignKey(blank=True, limit_choices_to={'role': 3}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='sales', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('amount', models.FloatField(blank=True)),
                ('payment_due', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='client_contract', to='crm_api.client')),
                ('sales_contact', models.ForeignKey(blank=True, limit_choices_to={'role': 3}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='sales_contract', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Not attributed'), (2, 'In progress'), (3, 'Ended')], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendees', models.IntegerField(blank=True, null=True)),
                ('event_dates', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=2000)),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='contract_event', to='crm_api.contract')),
                ('support_contact', models.ForeignKey(blank=True, limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='support', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]