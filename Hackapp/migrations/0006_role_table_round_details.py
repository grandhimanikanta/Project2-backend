# Generated by Django 3.1 on 2020-09-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackapp', '0005_auto_20200829_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='role_table',
            name='round_details',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
