from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# cão cão cão cão
# Simple image to string


# Create your views here.
def home(request):

    if request.method == 'POST':
        try:
            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)

                texto=pytesseract.image_to_string(Image.open(filename),lang='eng')
                os.remove(filename)
                return  render(request, 'next.html', {"texto": texto})
        except:
            return render(request, 'home.html', {"error": 'Passwords did not match'})
    else:
        return render(request, 'home.html', {"error": 'Passwords did not match'})

def next(request):
    texto=""
    return render(request,'next.html',{"texto":texto})