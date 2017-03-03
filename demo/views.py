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
            return render(request, 'index.html', {'invalid_error': '您的输入有误，请重新输入！'})
        print(form)
        # moviename = form.cleaned_data['moviename']
        # print(moviename)
        # return redirect('/demo/comment/?movie'+moviename)
        name = request.POST.get("moviename")
        print(name)
        data_source = MovieCommentCount.objects.filter(comment_movie__name=name)
        if not data_source:
            return render(request, 'index.html', {'invalid_error': '无法找到该电影的信息！'})
        return render(request, 'comment.html', {"data_source": data_source})
    elif request.method == 'GET':
        return render(request, 'index.html')


def CommentsCount(request):
    # CommentCountHandler(request)
    if request.method == 'POST':
        name = request.POST.get("moviename")
        # print(year)
        data_source = MovieCommentCount.objects.filter(comment_movie__name=name)
        if not data_source:
            return render(request, 'index_comment.html', {"comment_error": "无法找到有关影片的评论信息分析！"})
        return render(request, 'comment.html', {"data_source": data_source})
        # return render(request, 'comment.html')
    elif request.method == 'GET':
        return render(request, 'index_comment.html')


def Frequency(request):
    if request.method == 'POST':
        name = request.POST.get("moviename")
        print(name)
        data_source = CommentWordDictProducer(name)
        if not data_source:
            return render(request, 'index_frequency.html', {"freq_error": "无法找到该影片的词频分析情况！"})
        return render(request, 'frequency1.html', {"data_source": data_source})
        # return render(request, 'comment.html')
    elif request.method == 'GET':
        return render(request, 'index_frequency.html')


def CommentCountHandler(requst):
    # 返回json
    dict = {}
    for one in MovieCommentCount.objects.all():
        date = one.comment_date
        dict[date] = one.comment_count
    print(dict)
    return JsonResponse(dict)

def CommentWordDictProducer(name):
    raw_movie = MovieBase.objects.filter(name=name).first()
    if (raw_movie is None):
        pass
    raw_data = CommentWord.objects.filter(comment_movie=raw_movie)
    raw_dict = []
    print(raw_data)
    for ones in raw_data:
        print(ones)
        # raw_dict[ones.comment_word] = ones.comment_word_count
        raw_dict.append(ones)
        if len(raw_dict) > 40:
            break
    print(raw_dict)
    return raw_dict

