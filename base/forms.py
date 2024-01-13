from django import forms


class MessageForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=400)
