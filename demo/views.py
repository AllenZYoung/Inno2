from django.shortcuts import render, redirect
from .forms import MovieSearchForm
import simplejson
from django.template import Context, loader
from .models import *
from django.http import JsonResponse


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if not form.is_valid():
            pass
        print(form)
        # moviename = form.cleaned_data['moviename']
        # print(moviename)
        # return redirect('/demo/comment/?movie'+moviename)
        return redirect('/demo/commentsnum')
    else:
        return render(request, 'index.html')


def CommentsCount(request):
    # CommentCountHandler(request)
    return render(request, 'comment.html')


def Frequency(request):
    return render(request, 'frequency.html')

def CommentCountHandler(requst):
    dict = {}
    for one in MovieCommentCount.objects.all():
        date = one.comment_date
        dict[date] = one.comment_count
    print(dict)
    return JsonResponse(dict)
