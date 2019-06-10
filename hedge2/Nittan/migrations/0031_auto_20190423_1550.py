# Generated by Django 2.1.7 on 2019-04-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0030_auto_20190423_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessowner_registration',
            name='Investment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='businessowner_registration',
            name='Investor',
            field=models.CharField(default='None', max_length=90000000000000000),
        ),
        migrations.AddField(
            model_name='businessowner_registration',
            name='RepaidInvestment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='businessowner_registration',
            name='noOfInvestor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='investor_registration',
            name='Investment',
            field=models.IntegerField(default=0),
        ),
    ]
