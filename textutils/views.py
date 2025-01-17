# This file is created by me - samar

from django.http import HttpResponse
from django.shortcuts import render


def index (request):
    return render(request, 'index.html')
    
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    
    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            else:
                if char == ' ':
                    analyzed += char         
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed 
        # return render(request, 'analyze.html', params)
    
    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):    
                analyzed = analyzed + char
        params = {'purpose':'extraspaceremover', 'analyzed_text': analyzed}
        djtext = analyzed
            # Analyze the text
        # return render(request, 'analyze.html', params)
    
    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
            # Analyze the text
        # return render(request, 'analyze.html', params)
    
    if (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            params = {'purpose':'Removed new lines', 'analyzed_text': analyzed}
            # Analyze the text
    # else:
    if(removepunc != "on" and extraspaceremover !="on" and extraspaceremover !="on" and newlineremover !="on"):
        return HttpResponse("Please select any operation")

    return render(request, 'analyze.html', params)
