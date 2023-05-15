from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'مشاوره با ما '
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'work.moshavereh@gmail.com', ['rmaysam958@gmail.com'])
            except BadHeaderError:
                return HttpResponse('اشکال در ارسال ایمیل.')
            return HttpResponse('ایمیل شما با موفیت ارسال شد ')
    form = ContactForm
    return render(request, 'index.html', {'form': form})
