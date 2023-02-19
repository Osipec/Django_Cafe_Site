from django import forms
from .models import TableReserv

class ReservationForm(forms.ModelForm):
    user_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'name',
        'class': 'form-control',
        'id': 'name',
        'placeholder': 'Your Name',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    user_email = forms.CharField(max_length=254, widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Your Email',
        'data-rule': 'email',
        'data-msg': 'Please enter a valid email'
    }))
    user_phone = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={
        'type': 'text',
        'class': "form-control",
        'name': "phone",
        'id': "phone",
        'placeholder': "Your Phone",
        'data-rule':"minlen:4",
        'data-msg': "Please enter at least 4 chars"
    }))
    date = forms.CharField(widget=forms.DateInput(attrs={
        'type': 'text',
        'name': 'date',
        'class': 'form-control',
        'id': 'date',
        'placeholder': 'Date',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    time = forms.CharField(widget=forms.TimeInput(attrs={
        'type': 'text',
        'name': 'time',
        'class': 'form-control',
        'id': 'time',
        'placeholder': 'Time',
        'data-rule': 'minlen:4',
        'data-msg': 'Please enter at least 4 chars'
    }))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': 'number',
        'name': 'people',
        'class': 'form-control',
        'id': 'people',
        'placeholder': '# of people',
        'data-rule': 'minlen:1',
        'data-msg': 'Please enter at least 1 chars'
    }))
    message = forms.CharField(max_length=255, widget=forms.Textarea(attrs={
        'name': 'message',
        'type': 'message',
        'class': 'form-control',
        'rows': '5',
        'placeholder': 'Message',
    }))

    class Meta:
        model = TableReserv
        fields = ('user_name', 'user_email', 'user_phone', 'date', 'time', 'number_of_people', 'message')
