from django import forms

class patientForm(forms.Form):
    Name = forms.CharField()
    Gender = forms.CharField()
    DOB = forms.IntegerField()
    Cont_Num = forms.IntegerField()
