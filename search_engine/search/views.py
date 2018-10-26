from django.shortcuts import render
from django.views import generic
from django.conf import settings
import os, os.path
from django.core.files.storage import FileSystemStorage
from . import stem, indeces, tokenizer
import time

# Create your views here.

def index(request):

    return render(request, "search/index.html", {})

def results(request):
    t0 = time.time()
    s = request.GET['q']
    path, dirs, files = next(os.walk(os.path.join(settings.MEDIA_ROOT)))
    file_count = len(files)

    files_opened, tokens, links, describe = {},{},{},{}
    for file_number in range(1,file_count+1):
        files_opened['file_'+str(file_number)] = open(os.path.join(settings.MEDIA_ROOT, 'file'+str(file_number)+'.txt'), 'r', encoding="utf8").read()
        tokens['file_'+str(file_number)] = tokenizer.tokens(files_opened['file_'+str(file_number)],s)
    for file_number in range(1,file_count+1):
        if isinstance(tokens['file_'+str(file_number)], list):
            if tokens['file_'+str(file_number)][0] == True:
                links['file_'+str(file_number)] = {'file_'+str(file_number):'file'+str(file_number), 'describe':open(os.path.join(settings.MEDIA_ROOT, 'file'+str(file_number)+'.txt'), 'r', encoding="utf8").readline()[0:200] + '.....'}




    context = {
        's':s,
        'file':files_opened,
        'token':tokens,
        'links':links,
        'res_count':len(links.keys()),
        'describe':describe,
    }
    t1 = time.time()
    context['timer'] = round(t1-t0, 2)
    return render(request, "search/results.html", context)


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        path, dirs, files = next(os.walk(os.path.join(settings.MEDIA_ROOT)))
        file_count = len(files)+1
        request.FILES['myfile'].name = 'file'+str(file_count)+'.txt'
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'search/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url,
            'count_file':file_count,
        })
    return render(request, 'search/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'search/model_form_upload.html', {
        'form': form
    })
