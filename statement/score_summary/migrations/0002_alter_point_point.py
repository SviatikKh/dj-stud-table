# Generated by Django 3.2.7 on 2021-09-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score_summary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='point',
            field=models.CharField(blank=True, choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('зарах.', 'зарах.')], max_length=10, null=True, verbose_name='Оцінка'),
        ),
    ]
