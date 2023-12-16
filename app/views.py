from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages


def home(request):
    return render(request, 'index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Replace with the recipient's email address
        recipient_email = 'wamaejoseph392@gmail.com'
        emailObj = EmailMessage(
            f'{subject}',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            [recipient_email],
            reply_to=[email],
        )
        emailObj.send()
        messages.success(request, 'Your message was sent successfully!')
        return redirect('contacts')
    return render(request, 'contact.html')
