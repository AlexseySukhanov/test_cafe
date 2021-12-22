from django import forms
from .models import ModelFormRegistration


class FormRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text", 'name': "name", 'class': "form-control", 'id': "name",
                               'placeholder': "Your Name", 'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars",
                           }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                'type': "email", 'name': "email", 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                                    'data-rule':"email", 'data-msg': "Please enter a valid email"}))

    phone = forms.CharField(widget=forms.TextInput(attrs={
                                'type':"text", 'class': "form-control", 'name':"phone", 'id':"phone", 'placeholder':"Your Phone", 'data-rule':"minlen:4", 'data-msg':"Please enter at least 4 chars"}))

    message = forms.CharField(max_length=400,
                              widget=forms.TextInput(
                                  attrs={'type':'message', 'name':'message', 'class': 'form-control',
                                         'rows':5, 'placeholder':'Сообщение', 'required': 'required'}))
    date = forms.DateField(widget=forms.TextInput(
                                attrs={'type':'text', 'name':'date', 'class':'form-control', 'id':'date', 'placeholder':'Date', 'data-rule':'minlen:4','data-msg':'Please enter at least 4 chars'}))

    time = forms.DateTimeField(widget=forms.TextInput(
                                attrs={'type':'text', 'class':'form-control', 'name':'time', 'id':'time', 'placeholder':'Time', 'data-rule':'minlen:4', 'data-msg':'Please enter at least 4 chars'}))

    count_of_people = forms.CharField(widget=forms.TextInput(
                                attrs={'type':'number', 'class':'form-control', 'name':'people', 'id':'people', 'placeholder':'# of people', 'data-rule':'minlen:1', 'data-msg':'Please enter at least 1 chars'}
    ))



    class Meta:
        model = ModelFormRegistration
        fields = ('name', 'email', 'phone', 'date', 'time', 'count_of_people', 'message')

