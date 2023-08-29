from django.shortcuts import render , redirect
from .models import Article # 추가 
from .forms import ArticleForm  , CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    
    articles = Article.objects.all() 
    form = CommentForm()

    context = {
        'articles' : articles, 
        'form': form,
    }
    return render(request,'index.html', context)

@login_required
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

@login_required
def comment_create(request,article_id): 
    article = Article.objects.get(id=article_id)

    # 댓글작성 폼 
    form = CommentForm(request.POST)
    
    if form.is_valid(): # 댓글을 잘 작성했다면 
        comment = form.save(commit=False)
        # 아직 user값 없어서 저장하지마
        comment.user = request.user
        comment.article = article 
        comment.save()

        return redirect('articles:index')