# Generated by Django 3.2.5 on 2021-07-31 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['expire_date']},
        ),
    ]
