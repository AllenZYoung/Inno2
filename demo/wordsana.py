# coding=utf-8
import jieba
import jieba.analyse
import os
from collections import Counter

# from django.conf import settings
# from contentui import settings
# settings.configure(settings)
import django
import sys

import pymysql
import os

# pro_dir = os.getcwd()  #如果放在project目录，就不需要在配置绝对路径了
# sys.path.append(pro_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Inno2.settings')
django.setup()
# 打开数据库连接
# import pymysql.cursors
#
# # Connect to the database
# connection = pymysql.connect(host='localhost',
#                              user='django1',
#                              password='password',
#                              db='scrapydec',
#                              # charset='utf8mb4',
#                              # cursorclass=pymysql.cursors.DictCursor)
#                              )
# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `moviecommentcount` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()

from demo.models import *

# TODO 存储词频
# movie = MovieBase.objects.filter(name='星际穿越').first()
#
# file_path = os.path.join('/Users/zhangyang/PycharmProjects/scrap1/nst', 'review.txt')
# dict_name = os.path.join('/Users/zhangyang/PycharmProjects/scrap1/nst', 'dict.txt')
# jieba.load_userdict(dict_name)
# text = ''
# with open(file_path, 'r') as myfile:
#     text += myfile.read().replace('\n', '')
# # # print(text)
# print('---------------------------')
# fullmode = jieba.cut(text)
#
# words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
# c = Counter(words)
# for word_freq in c.most_common(50):
#     word, freq = word_freq
#     print(word, freq)
#     data_object = CommentWord(comment_movie=movie,
#                               comment_word=word, comment_word_count=freq)
#     data_object.save()
# # print("text:"+"/".join(fullmode))
# # findWord = jieba.analyse.extract_tags(text, topK=30, withWeight=True)
# # for word, weight in findWord:
# #     print("{}\t{}".format(word, weight))
#
# print('---------------------------')
# comments here
# import os
#
#
# import nst.markov_speaking as markov_speaking
# file_path = '/Users/zhangyang/PycharmProjects/scrap1/nst/'
# path = os.path.join(file_path,'maoxuan.txt')
# print(path)
#
# p = markov_speaking.Markov(path, 1)
# for i in range(1, 20):
#     sentence = p.say(6)

# from __future__ import print_function, unicode_literals
import json
import requests

# SENTIMENT_URL = 'http://api.bosonnlp.com/sentiment/analysis'
# # 注意：在测试时请更换为您的API Token
# headers = {'X-Token': 'kyzJdAUy.11008.siVn5gRGFfwz'}
#
# s = ['他是个傻逼', '美好的世界']
# data = json.dumps(s)
# resp = requests.post(SENTIMENT_URL, headers=headers, data=data.encode('utf-8'))
#
# print(resp.text)
# new_movie = MovieBase(name='湄公河行动', doubanurl='https://movie.douban.com/subject/25815034/',
#                       director='林超贤',
#                       commenturl='https://movie.douban.com/subject/25815034/comments?sort=new_score&status=P')
# new_movie.save()
movie=MovieBase.objects.filter(name='湄公河行动').first()
import random

for i in range(1, 100):
    print(random.uniform(1, 10))

# for i in range(1,100):
# word, freq = word_freq
# print(word, freq)
a = 10
for b in range(1, 28):
    if b < 10:
        value = random.uniform(4, 6.3)
    elif b < 20:
        value = random.uniform(6, 7.5)
    else:
        value = random.uniform(7, 8.2)

    date_now = '2016-%s-%s' % (a, b)
    print(date_now)
    data_object = MovieEmotion(emotion_movie=movie,
                               emotion_date=date_now, emotion_value=value)
    data_object.save()
