from django import forms
from captcha.fields import CaptchaField
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }