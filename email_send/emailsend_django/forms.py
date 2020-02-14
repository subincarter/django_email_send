from django import forms
class emailSendForm(forms.Form):
    subject=forms.CharField()
    body=forms.CharField()
    # email=forms.EmailField()
    # phone=forms.IntegerField()
    # file=forms.FileField()
    image = forms.FileField()
