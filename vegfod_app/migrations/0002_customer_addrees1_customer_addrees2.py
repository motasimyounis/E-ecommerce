# Generated by Django 4.1.5 on 2023-02-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegfod_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='addrees1',
            field=models.TextField(default='such as: Salah_aldeen- in nuserate', max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='addrees2',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
