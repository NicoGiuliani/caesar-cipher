from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def encode(request):
    if request.method == 'POST':
        plaintext_message = request.POST['plaintext_message'].upper()
        shift = 5

        english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        encoded_message = list(plaintext_message[:])

        for i in range(len(plaintext_message)):
            current_character = plaintext_message[i]
            alphabet_index = english_alphabet.find(current_character)
            if alphabet_index >= 0:
                encoded_message[i] = english_alphabet[(alphabet_index + shift) % 26]

        encoded_message = ''.join(encoded_message)

        return render(request, 'encode.html', {'encoded_message': encoded_message})
