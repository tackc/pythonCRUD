# Generated by Django 3.1.1 on 2020-09-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestType', models.CharField(max_length=10)),
                ('requestTime', models.DateTimeField(verbose_name='date created')),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
    ]
