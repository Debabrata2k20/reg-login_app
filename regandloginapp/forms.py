from django import forms
from .models import RegModel
class RegModelForm(forms.ModelForm):
    class Meta:
        model=RegModel
        fields=['FirstName','LastName','UserName','Password','CPassword','EmailId','MobileNo']
        widgets={'Password':forms.PasswordInput(),'CPassword':forms.PasswordInput()}
class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=10)
    Password = forms.CharField(max_length=10, widget=forms.PasswordInput())