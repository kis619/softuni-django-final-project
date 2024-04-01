from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

UserModel = get_user_model()


class LetUsTalkUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class LetUsTalkUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
