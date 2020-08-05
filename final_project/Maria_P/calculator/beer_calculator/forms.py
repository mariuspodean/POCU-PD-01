from django import forms

from .models import Ingredient_Type, Ingredient, Recipe_Type

class Add_Ingredient_Form(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    ingredient_type = forms.ModelChoiceField(queryset=Ingredient_Type.objects.all(), label='Type')
    quantity = forms.DecimalField(label='Quantity (g)', max_digits=10, decimal_places=2)
    price = forms.DecimalField(label='Price for 100 g (RON)', max_digits=10, decimal_places=2)
 #   add_date = forms.DateTimeField(label='Date & Time Added')
    update_date = forms.DateTimeField(label='Date & Time Updated')

class Add_Recipe_Form(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    recipe_type = forms.ModelChoiceField(queryset=Recipe_Type.objects.all(), label='Type')
    ingredient = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), label='Ingredient')
#    quantity = forms.DecimalField(label='Quantity (g)', max_digits=10, decimal_places=2)
 #   add_date = forms.DateTimeField(label='Date & Time Added')
    update_date = forms.DateTimeField(label='Date & Time Updated')