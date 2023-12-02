# Generated by Django 4.2.7 on 2023-12-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0003_remove_pokemoncards_card_types_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncards',
            name='card_type',
            field=models.CharField(blank=True, choices=[('Fire', 'Fire'), ('Water', 'Water'), ('Grass', 'Grass'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Ice', 'Ice'), ('Dragon', 'Dragon'), ('Dark', 'Dark'), ('Normal', 'Normal'), ('Fighting', 'Fighting'), ('Flying', 'Flying'), ('Poison', 'Poison'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Bug', 'Bug'), ('Ghost', 'Ghost'), ('Steel', 'Steel'), ('Fairy', 'Fairy')], max_length=100, null=True),
        ),
    ]
