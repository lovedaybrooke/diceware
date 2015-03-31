from django.shortcuts import render

import generate

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html', {
            "passphrase": generate.makePassphrase()})