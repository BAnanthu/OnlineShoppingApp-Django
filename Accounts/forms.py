from django import forms

class UserSignupForm(forms.Form):
    user_name = forms.CharField(max_length=50)
    user_email = forms.EmailField()
    user_password = forms.CharField(max_length=15)
    user_confirm_password = forms.CharField(max_length=15)

    def clean_std_name(self):
        value = self.cleaned_data['user_name']
        if value.isupper():
            raise forms.ValidationError('name must be lower case')
        return value