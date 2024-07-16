from django.contrib.auth.forms import UserCreationForm
from .models import User, Player
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','password1','password2']

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'avatar', 'email', 'bio', 'players']



