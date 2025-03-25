# Generated by Django 3.2.8 on 2021-10-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_product_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
