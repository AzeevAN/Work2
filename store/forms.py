from .models import Store
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = UserCreationForm.Meta.fields + ('inn', 'year_open', )

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Store
        fields = UserChangeForm.Meta.fields # допишу что понадобится