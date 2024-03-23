# Generated by Django 5.0.3 on 2024-03-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=20)),
                ('branch', models.CharField(choices=[('IT', 'information technology'), ('EXT', 'electrical'), ('MECH', 'mechanical'), ('CV', 'civil')], max_length=7)),
                ('date', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]