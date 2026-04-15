from django import forms
from basic_app.models import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfo
        exclude = ('user',)