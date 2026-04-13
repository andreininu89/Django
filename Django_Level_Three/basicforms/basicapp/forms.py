from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError("Name needs to start with Z")


class NameForm(forms.Form):
    # name = forms.CharField(label="Your name", max_length=100, validators=[check_for_z])
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email", max_length=100)
    verify_email = forms.EmailField(label="Verify Email", max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 5}))
    bot_catcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        validators=[validators.MaxLengthValidator(0)],
    )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError("Email and Verify Email are not matching")

    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data["bot_catcher"]
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("You are not allowed to use this bot")
    #     return bot_catcher
