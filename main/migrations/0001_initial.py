# Generated by Django 5.1.3 on 2024-12-20 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpyCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('experience_years', models.IntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missions', to='main.spycat')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('notes', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='main.mission')),
            ],
        ),
    ]
