# Generated by Django 2.1.4 on 2018-12-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181205_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='planet',
            name='to_display',
            field=models.BooleanField(default=True),
        ),
    ]
