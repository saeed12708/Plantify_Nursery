# Generated by Django 5.2 on 2025-05-06 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0002_fertilizer_cart_fertilizer_fav_id_fertilizer_order_and_more'),
        ('users_app', '0006_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('seed_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='seed_images/')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seed_carts', to='users_app.cart')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seed_favorites', to='users_app.favorite')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seed_orders', to='users_app.order')),
            ],
        ),
    ]
