# Generated by Django 4.2.6 on 2023-10-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitApp', '0002_product_avg_norm_rating_product_count_norm_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='neg_words',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pos_words',
        ),
        migrations.AddField(
            model_name='product',
            name='neg_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='neg_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='neg_3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pos_1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pos_2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pos_3',
            field=models.CharField(max_length=20, null=True),
        ),
    ]