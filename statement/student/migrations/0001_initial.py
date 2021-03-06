# Generated by Django 3.2.7 on 2021-12-06 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('score_summary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, verbose_name="Ім'я")),
                ('surname', models.CharField(blank=True, max_length=20, verbose_name='Прізвище')),
                ('patronymic', models.CharField(blank=True, max_length=20, verbose_name='По-батькові')),
                ('group', models.ForeignKey(blank=True, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='score_summary.group', verbose_name='Група')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
            },
        ),
    ]
