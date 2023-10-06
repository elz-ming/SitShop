# Generated by Django 4.2.6 on 2023-10-06 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('merchant_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='sitApp.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('review_text', models.TextField()),
                ('customer_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='sitApp.customer')),
                ('product_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='sitApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('merchant_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('merchant_name', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='sitApp.customer')),
            ],
        ),
    ]