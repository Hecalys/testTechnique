# Generated by Django 3.0.6 on 2020-05-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200525_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_gtin',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
