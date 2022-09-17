# Generated by Django 3.1.4 on 2021-06-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LongtoShort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField(max_length=250)),
                ('shorturl', models.CharField(max_length=25, unique=True)),
            ],
        ),
    ]
