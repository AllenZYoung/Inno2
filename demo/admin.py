from django.contrib import admin
from .models import *
admin.site.register(MovieBase)
admin.site.register(CommentBase)
admin.site.register(MovieCommentCount)
# Register your models here.
