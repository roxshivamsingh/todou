# Generated by Django 2.2.16 on 2020-11-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201129_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
