from django.shortcuts import render , redirect
from .models import Article # 추가 
from .forms import ArticleForm 

# Create your views here.
def index(request):
    
    articles = Article.objects.all() # 전체게시글 조회 

    context = {
        'articles' : articles, 
    }
    return render(request,'index.html', context)

def create(request): 
    if request.method == 'POST': 
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            article = form.save(commit=False)
            # 잠깐 user정보값이 없으니, 저장하기전에 멈춰 = 그 값을 article에 넣음 
            article.user = request.user 
            # user에는 현재 로그인한 사람에 대한 정보가 있다. 
            # 이제 저장할 준비가 되었다. 
            article.save()
            return redirect('articles:index')

    else: 
        form = ArticleForm()
    
    context = {
        'form': form, 
    }

    return render(request, 'form.html', context)