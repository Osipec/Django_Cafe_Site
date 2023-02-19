from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password_1 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password_1')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Wrong login or password')
        else:
            raise forms.ValidationError('Wrong login or password')
        return super().clean()


class UserRegistration(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password_1 = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',)

    def clean_password_2(self):
        data = self.cleaned_data
        if data.get('password_1') == data.get('password_2'):
            return data['password_2']
        raise forms.ValidationError('Error in passwords')

