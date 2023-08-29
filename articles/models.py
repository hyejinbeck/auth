from django.db import models
from accounts.models import User 
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    # 제목과 내용을 갖는다. 
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 장고가 자동으로 추가해주는 컬럼

    # 유저모델을 참조하는 경우 - 3번째방법 
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

class Comment(models.Model): 
    # 댓글과 내용을 갖는다 
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 장고가 자동으로 추가해주는 칼럼 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    #우리는 여기에 get_user_model과 연결할거야.