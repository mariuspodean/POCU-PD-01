from django import forms
from .models import Pacient, Drugs

class AddPacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields =[
                'name_pacient', 
                'disease',
                'email_address'
        ]
        widgets ={
            'name_pacient': forms.TextInput(attrs={'class': 'form-control'}),
            'disease': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control'})
        }
    def clean_name(self):
        name_pacient = self.cleaned_data.get('name_pacient')
        for instance in Pacient.objects.all():
            if instance.name_pacient == name_pacient:
                raise forms.ValidationError()
        return name_pacient

class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields =[
                'name_of_drug', 
                'data_of_expiration',
                'stock'
        ]
        widgets ={
            'name_of_drug': forms.TextInput(attrs={'class': 'form-control'}),
            'data_of_expiration': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.TextInput(attrs={'class': 'form-control'})
        }
    
