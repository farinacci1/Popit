from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ModelForm
from .models import User



class UserAdminCreationForm(ModelForm):
    Password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["Password"])
        user.active = False
        if commit:
            user.save()
        return user


class UserAdminChangeForm(ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email','password', 'active', 'admin')

    def clean_password(self):
        return self.initial["password"]


class RegisterForm(ModelForm):
    Pass  =  forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 100, 'required': True, 'id':'password_field','placeholder': 'Password'}))
    Pass2 =  forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 100, 'required': True, 'id':'password_field_2','placeholder': 'Match Password'}))
    class Meta:
        model = User
        fields = (
            'email',
        )
    def clean_pass2(self):
        pass1 = self.cleaned_data.get('Password')
        pass2 = self.cleaned_data.get('pass2')
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError("Passwords don't match")
        return pass2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["Pass"])
        user.active = False
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={
            'id': 'Email_field',
            'name': 'Email',
            'placeholder': 'Email'})
