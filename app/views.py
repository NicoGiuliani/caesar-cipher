from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datetime import datetime
from .models import Encoded_Message
import random


# Create your views here.
def index(request):
    if request.method == 'POST':
        encoded_message = request.POST['encoded_message']
        user_id = request.POST['user_id']
        user = User.objects.filter(id=user_id)[0]

        message_id_selected = False 
        while message_id_selected == False:
            message_id = random.randint(1, 1000000000)
            if Encoded_Message.objects.filter(id=message_id).exists() == False:
                message_id_selected = True

        message = Encoded_Message(id=message_id, owner=user, text=encoded_message, creation_date=datetime.now())
        message.save()
        messages.success(request, 'Message saved successfully')
        return redirect('/')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_verification = request.POST['password_verification']

        if password == password_verification:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email is already in use', )
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'User successfully created')
                    return redirect('login')
        else:
            messages.info(request, 'Passwords did not match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('/')
        else: 
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')


def view(request):
    username = request.POST['username']
    user = User.objects.filter(username=username)[0]
    encoded_message_list = Encoded_Message.objects.filter(owner=user)
    return render(request, 'view.html', {'encoded_message_list': encoded_message_list})


def encode(request):
    if request.method == 'POST':
        plaintext_message = request.POST['plaintext_message'].upper()
        shift = int(request.POST['shift_value'])

        english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encoded_message = list(plaintext_message[:])

        for i in range(len(plaintext_message)):
            current_character = plaintext_message[i]
            alphabet_index = english_alphabet.find(current_character)
            if alphabet_index >= 0:
                encoded_message[i] = english_alphabet[(alphabet_index + shift) % 26]

        encoded_message = ''.join(encoded_message)

        return render(request, 'encode.html', {'encoded_message': encoded_message})


def decode(request):
    encoded_message = request.POST['encoded_message'].upper()
    plaintext_message = list(encoded_message[:])

    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = int(request.POST['shift_value'])

    for i in range(len(encoded_message)):
        current_character = encoded_message[i]
        alphabet_index = english_alphabet.find(current_character)
        if alphabet_index >= 0:
            plaintext_message[i] = english_alphabet[(alphabet_index - shift) % 26]

    plaintext_message = ''.join(plaintext_message)

    return render(request, 'decode.html', {'plaintext_message': plaintext_message})

