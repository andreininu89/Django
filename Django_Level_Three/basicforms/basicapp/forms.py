from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField(label="Your email", max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
