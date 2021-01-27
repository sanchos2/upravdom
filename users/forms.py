from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):  # noqa: D101

    class Meta:  # noqa: D106, WPS306

        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):  # noqa: D101

    class Meta:  # noqa: D106, WPS306

        model = CustomUser
        fields = UserChangeForm.Meta.fields
