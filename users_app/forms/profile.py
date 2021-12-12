from django.contrib.auth.models import User
from django.forms import ModelForm

from ..models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
                'email',
                'first_name',
                'last_name'
                )

    def save(self, commit=True, *args, **kwargs):
        profile = super(ProfileForm, self).save(commit=False, *args, **kwargs)
        if commit:
            profile.save()
        return profile

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
