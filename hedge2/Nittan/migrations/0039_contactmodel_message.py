# Generated by Django 2.1.7 on 2019-04-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0038_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='message',
            field=models.CharField(default='hello', max_length=90000000000),
            preserve_default=False,
        ),
    ]
