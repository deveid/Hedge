# Generated by Django 2.1.7 on 2019-03-26 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0004_auto_20190325_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='Nila', max_length=50),
            preserve_default=False,
        ),
    ]
