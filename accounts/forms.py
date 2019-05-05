from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    # def __init__(self):
        # super(UserCreationForm, self).__init__()
        # self.fields['username'].widget.attrs.pop("autofocus", None)
       
    #image = forms.FileField(upload_to="photos/", default="profile.jpg")
    class Meta():
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if not first_name and not last_name and not username and email and not password1 and not password2:
            raise forms.ValidationError('You Should Fill fields in order to Register YourSelf!')