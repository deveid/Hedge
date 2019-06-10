# Generated by Django 2.1.7 on 2019-04-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0026_delete_contactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='business',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='paidInvestor',
        ),
        migrations.AddField(
            model_name='payment',
            name='Bank_Teller',
            field=models.ImageField(default='asa', upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='figiID',
            field=models.CharField(default='F-10293', max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='Amount',
            field=models.IntegerField(default=200000),
        ),
    ]
