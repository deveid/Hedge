# Generated by Django 2.1.7 on 2019-04-24 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0033_auto_20190424_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor_registration',
            name='Earnings',
            field=models.CharField(default='0', max_length=900000000000000000000000000000),
        ),
    ]
