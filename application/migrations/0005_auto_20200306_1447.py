# Generated by Django 3.0.3 on 2020-03-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20200306_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='age',
            field=models.IntegerField(default='1'),
        ),
    ]
