# Generated by Django 3.2.9 on 2022-08-11 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('h1', models.TextField()),
                ('h2', models.TextField()),
            ],
        ),
    ]
