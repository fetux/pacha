from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField()
    mail = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        send_mail(
            'Message from Nucapacha.com',
            self.cleaned_data['message'],
            self.cleaned_data['mail'],
            ['fetu@fetux.net'],
            #['contact@nucapacha.com'],
            fail_silently=False,
        )
