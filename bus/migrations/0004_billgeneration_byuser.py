# Generated by Django 3.0.7 on 2020-11-17 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_billgeneration'),
    ]

    operations = [
        migrations.AddField(
            model_name='billgeneration',
            name='byuser',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
