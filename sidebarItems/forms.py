from django import forms
from . import models

#All the forms are present here
#Form for Stock Card
class stockCardForm(forms.ModelForm):
    class Meta:
        model = models.stockCard
        fields = ['name', 'measurement_unit', 'opening_stock', 'description']

    #Defining the dropdown options ('value stored in db', 'value displayed to the user')
    MEASUREMENT_UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('l', 'Litres'),
        ('m', 'Metres'),
        ('sets', 'sets'),
        ('units', 'units')
    ]

    measurement_unit = forms.ChoiceField(
        choices=MEASUREMENT_UNIT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )
