from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import user
from django import forms

class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = user
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfileForm(UserProfileForm):


    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'



