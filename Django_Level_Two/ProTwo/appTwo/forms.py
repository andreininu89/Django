from django import forms
from appTwo.models import User


class NewUserForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name:", max_length=100)
    last_name = forms.CharField(label="Last Name:", max_length=100)
    email = forms.EmailField(label="Email Address:", max_length=100)
    confirm_email = forms.EmailField(label="Confirm Email Address:", max_length=100)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        confirm_email = all_clean_data["confirm_email"]

        if email != confirm_email:
            raise forms.ValidationError("Emails are not matching")

    class Meta:
        model = User
        # fields = ("first_name", "last_name", "email")
        fields = "__all__"
