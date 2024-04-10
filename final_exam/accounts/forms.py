from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from final_exam.accounts.models import LetUsTalkUserProfile

UserModel = get_user_model()


class LetUsTalkUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class LetUsTalkUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class LetUsTalkUserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class LetUsTalkUserProfileForm(forms.ModelForm):
    class Meta:
        model = LetUsTalkUserProfile
        fields = ['first_name', 'last_name', 'avatar', 'bio', 'birth_date']

        widgets = {
            'birth_date': forms.DateInput(format=('%Y-%m-%d'),
                                          attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                 'type': 'date'}),
        }
