from django import forms
from .models import Comments

class commentForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control", 'name':"name",'id':"name",'type':"text",
                                                                        'placeholder':"Name"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control w-100", 'name':"comment",'id':"comment", 'cols':"30",'rows':"9" ,'placeholder':"Write Comment"}))
    email=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control",'name':"email",'id':"email",'type':"email",
                                            'placeholder':"Email"}))
    class Meta:
        model=Comments
        fields=['content','name','email']

