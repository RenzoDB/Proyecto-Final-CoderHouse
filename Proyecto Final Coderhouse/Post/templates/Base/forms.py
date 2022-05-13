from django import forms
from Post.models import *

class CreateForm(forms.Form):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'descripcion' : forms.Form.TextInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}),
            'titulo': forms.Form.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.Form.NumberInput(attrs={'class': 'form-control'}),
            
        }