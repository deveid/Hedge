# Generated by Django 2.1.7 on 2019-04-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nittan', '0024_auto_20190415_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=100000000)),
            ],
        ),
    ]
