from django import forms
from .models import Faqs

class FaqsForm(forms.ModelForm):
    question = forms.CharField(max_length=100, required=True)
    answer = forms.CharField(max_length=200, required=True)
    isActive = forms.BooleanField()

    class Meta:
        model = Faqs
        fields = ['question','answer','isActive']