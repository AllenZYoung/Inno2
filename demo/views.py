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
        name = request.POST.get("moviename")
        print(name)
        data_source = MovieCommentCount.objects.filter(comment_movie__name=name)
        return render(request, 'comment.html', {"data_source": data_source})
    elif request.method == 'GET':
        return render(request, 'index.html')


def CommentsCount(request):
    # CommentCountHandler(request)
    if request.method == 'POST':
        name = request.POST.get("moviename")
        # print(year)
        data_source = MovieCommentCount.objects.filter(comment_movie__name=name)
        return render(request, 'comment.html', {"data_source": data_source})
        # return render(request, 'comment.html')
    elif request.method == 'GET':
        return render(request, 'index_comment.html')


def Frequency(request):
    return render(request, 'frequency.html')


def CommentCountHandler(requst):
    # 返回json
    dict = {}
    for one in MovieCommentCount.objects.all():
        date = one.comment_date
        dict[date] = one.comment_count
    print(dict)
    return JsonResponse(dict)
