# Generated by Django 2.1.7 on 2019-04-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0037_auto_20190424_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
    ]
