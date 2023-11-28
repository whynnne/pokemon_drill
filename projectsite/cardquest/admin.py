from django.contrib import admin
from .models import Trainer
from .models import PokemonCards

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email")
    search_fields = ("name", "location",)

@admin.register(PokemonCards)
class PokemonCardsAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack", "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities")
    search_fields = ("name", "rarity", "card_type",)