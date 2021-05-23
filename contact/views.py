from django.shortcuts import render
from .forms import EmailForm

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
                  message, EMAIL_HOST_USER, ['ashok.budha2015@gmail.com'], fail_silently=False)
        messages.success(request, f'Your email has been sent !!')
        return redirect('blog_index')
    return render(request,'contact.html',{'form':sub})
