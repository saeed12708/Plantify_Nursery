# Generated by Django 5.2 on 2025-05-05 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_blog_location_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('method_type', models.CharField(max_length=50)),
                ('provider', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('is_default', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to='users_app.order')),
            ],
        ),
    ]
