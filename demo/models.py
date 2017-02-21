from django.db import models


# Create your models here.

class MovieBase(models.Model):
    name = models.CharField(max_length=100, null=False)
    doubanurl = models.CharField(max_length=100, null=False, primary_key=True)
    director = models.CharField(max_length=30, null=False)
    commenturl = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'moviebase'

    # tostring
    def __str__(self):
        return 'moviename: %s' % (self.name)


class CommentBase(models.Model):
    comment_date = models.CharField(max_length=10, null=False)
    comment_content = models.CharField(max_length=500, null=False)
    # comment_id = models.CharField(max_length=100, null=False)
    comment_movie = models.ForeignKey(MovieBase)

    class Meta:
        db_table = 'commentbase'

    # tostring
    def __str__(self):
        return 'comment: %s' % (self.comment_content)

class MovieCommentCount(models.Model):
    comment_movie = models.ForeignKey(MovieBase)
    comment_movie_name = MovieBase.name
    comment_date = models.CharField(max_length=10, null=False)
    comment_count = models.IntegerField()

    class Meta:
        db_table = 'moviecommentcount'

class CommentWord(models.Model):
    comment_movie = models.ForeignKey(MovieBase)
    comment_movie_name = MovieBase.name
    comment_word = models.CharField(max_length=50, null=False)
    comment_word_count = models.IntegerField()

    class Meta:
        db_table = 'moviecommentword'
