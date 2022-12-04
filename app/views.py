from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def encode(request):
    if request.method == 'POST':
        plaintext_message = request.POST['plaintext_message']
        encoded_message = plaintext_message[::-1]
        return render(request, 'encode.html', {'encoded_message': encoded_message})