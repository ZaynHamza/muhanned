# Generated by Django 4.0.3 on 2022-05-24 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beauty',
            options={'ordering': ['-pub_date'], 'verbose_name_plural': 'Beauties'},
        ),
    ]
