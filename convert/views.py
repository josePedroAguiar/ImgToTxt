from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import os
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
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

            if request.FILES['myfile']:
                myfile = request.FILES['myfile']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)

                texto=pytesseract.image_to_string(Image.open(filename),lang='eng')
                os.remove(filename)
                return  render(request, 'next.html', {"texto": texto})
            return render(request, 'home.html', {"error": 'Passwords did not match'})
    else:
        return render(request, 'home.html', {"error": 'Passwords did not match'})

def next(request):
    texto=""
    return render(request,'next.html',{"texto":texto})

def start(request):
    return render(request, 'start.html')

def download(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = '/test.txt'
    # Define the full file path
    filepath = BASE_DIR + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response