# Generated by Django 3.0.6 on 2020-05-25 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200525_1048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='product',
        ),
    ]
