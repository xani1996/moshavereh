from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='نام شما')
    last_name = forms.CharField(max_length=50, label='نام خانوادگی')
    phone_number = forms.CharField(max_length=20, label='شماره تلفن شما')
    email_address = forms.EmailField(max_length=150, label='ایمیل ادرس شما')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label='علت مراجعه ')
