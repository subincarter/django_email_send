from django.shortcuts import render
from django.core.mail.message import EmailMessage
from django.http import HttpResponse
from .forms import emailSendForm
from .models import *
# Create your views here.
# def send(request):
#     email=EmailMessage(subject='Coffeehouse specials',
#                        body='we would like to let you know about this week\s specials...',
#                        from_email='subinkumar48@gmail.com',
#                        to=['subinkumar48@gmail.com'])
#     email.send()
#     return HttpResponse('send successfully')


# def newEmail(request):
#     myemail=emailSend()
#     if request.method=='POST':
#         sendForm=emailSend(request.POST,request.FILES)
#         if sendForm.is_valid():
#             subject=sendForm.cleaned_data['subject']
#             body = sendForm.cleaned_data['body']
#             file1=sendForm.cleaned_data['file']
#             email = EmailMessage(subject=subject,
#                                  body=body,
#                                  from_email='subinkumar48@gmail.com',
#                                  to=['subinkumar48@gmail.com'])
#
#
#             email.attach(file1.name,file1.read(),file1.content_type)
#             email.send()
#             return HttpResponse("email send")
#
#     return render(request,'emailform.html',{'data':myemail})
def upload(request):
    form=emailSendForm()
    if (request.method=="POST"):
        form=emailSendForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj=emailSend()
            obj.subject=form.cleaned_data['subject']
            obj.body=form.cleaned_data['body']
            obj.image=form.cleaned_data['image']
            obj.save()
            return HttpResponse('saved')
    return render(request,'emailform.html',{'form':form})

def imageview(request):
    emailview=emailSend.objects.all()
    return render(request,'imageview.html',{'emails':emailview})