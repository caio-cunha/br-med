from django import forms

class DateForm(forms.Form):
    date_initial = forms.DateField()
    date_final = forms.DateField()
