# Generated by Django 3.0.2 on 2020-01-31 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza1', '0003_auto_20200131_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]
