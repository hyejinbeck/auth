from django.shortcuts import render
from .models import Article # 추가 

# Create your views here.
def index(request):
    
    articles = Article.objects.all() # 전체게시글 조회 

    context = {
        'articles' : articles, 
    }
    return render(request,'index.html', context)