# Generated by Django 5.0.6 on 2024-05-30 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_package_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]