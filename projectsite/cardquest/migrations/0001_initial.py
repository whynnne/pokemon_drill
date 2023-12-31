# Generated by Django 4.2.7 on 2023-11-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
