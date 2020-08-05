from django.contrib import admin

from .models import IngredientType, Ingredient, RecipeType, Recipe, Cost


class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ingredient_type', 'quantity', 'price', 'update_date_time')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class RecipeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'recipe_type', 'update_date_time')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'quantity', 'cost')
    search_fields = ('recipe__name', 'ingredient__name')

admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeType, RecipeTypeAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Cost, CostAdmin)
