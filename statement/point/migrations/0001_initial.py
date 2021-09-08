# Generated by Django 3.2.7 on 2021-09-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(blank=True, max_length=10, verbose_name='Оцінка')),
            ],
            options={
                'verbose_name': 'Оцінка',
                'verbose_name_plural': 'Оцінки',
            },
        ),
    ]
