from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
def index(request):
    return HttpResponse("Xin chao")

def addPost(request):
    postForm = PostForm()
    return render(request, 'news/addPost.html', {'form': postForm})

def saveNewPost(request):
    if(request.method == 'POST'):
        g = PostForm(request.POST)
        if(g.is_valid()): 
            g.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("inValid Form")
    else: 
        return HttpResponse("Must be POST request")    