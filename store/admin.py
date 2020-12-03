from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MyUserChangeForm, MyUserCreationForm
from .models import Store


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = Store
    list_display = ["username", "email", "inn", 'year_open']


admin.site.register(Store, MyUserAdmin)