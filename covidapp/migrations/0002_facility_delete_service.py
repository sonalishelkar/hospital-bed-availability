# Generated by Django 4.0.4 on 2022-05-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
