# Generated by Django 2.1.7 on 2019-04-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0028_auto_20190420_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='Amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payments',
            name='Bank_Teller',
            field=models.ImageField(default='/home/david/miniconda3/hedge2/media/media/1.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='figiID',
            field=models.CharField(default='F-00000', max_length=10),
        ),
    ]
