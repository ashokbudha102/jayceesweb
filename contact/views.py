from django.shortcuts import render,redirect
from .forms import EmailForm
from django.core.mail import send_mail
from django.contrib import messages
from jaycees.settings import EMAIL_HOST_USER

# Create your views here.
def contact(request):
    sub = EmailForm()
    if request.method == 'POST':
        sub = EmailForm(request.POST)
        subject = str(sub['subject'].value())
        message = str(sub['body'].value())
        recepient = str(sub['email'].value())
        name = str(sub['name'].value())
        message = "Name:"+name+'\n'+"SENDER:"+recepient+'\n'+"MESSAGE:"+message
        send_mail(subject,
                  message, EMAIL_HOST_USER, ['devchulijci44@gmail.com'], fail_silently=False)
        messages.success(request, f'Your email has been sent !!')
        return redirect('/')
    return render(request,'contact.html',{'form':sub})

def about(request):
    return render(request, 'about.html',{})
