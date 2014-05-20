from django.forms import ModelForm
from igame.models import Game,Shop,Producer

class gameForm(ModelForm):
    class Meta:
        model = Game
        exclude = ('user', 'date',)

class shopForm(ModelForm):
    class Meta:
        model = Shop
        exclude = ('user', 'date',)

class producerForm(ModelForm):
    class Meta:
        model = Producer
        exclude = ('user', 'date',)
