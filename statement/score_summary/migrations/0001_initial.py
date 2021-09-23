# Generated by Django 3.2.7 on 2021-09-22 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, max_length=20, verbose_name='Група')),
                ('curator', models.CharField(blank=True, max_length=50, null=True, verbose_name='Куратор')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(blank=True, choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('зарах.', 'зарах.')], max_length=10, null=True, verbose_name='Оцінка')),
            ],
            options={
                'verbose_name': 'Оцінка',
                'verbose_name_plural': 'Оцінки',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50, verbose_name='Предмет')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher', verbose_name='Викладач')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предмети',
            },
        ),
        migrations.CreateModel(
            name='Scoresummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='score_summary.group', verbose_name='Група')),
                ('point', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='score_summary.point', verbose_name='Оцінка')),
            ],
        ),
    ]
