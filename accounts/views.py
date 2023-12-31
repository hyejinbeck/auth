from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.user.is_authenticated: 
        # 너 로그인 한사람이야? 그러면 
        return redirect('articles:index')
        # 그럼 너 그냥 인덱스로 가  여기 오지마 
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(user, user.username, user.password)
            auth_login(request,user)
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'account_form.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # http://127.0.0.1:8000/accounts/login/?next=/articles/create/ 
            next_url = request.GET.get('next') # => /articles/create 

            return redirect(next_url or 'articles:index')
            # articles의 index로 보내기  

            # next인자가 url에 있을 때 -> '/articles/create' or 'articles:index'
            # 파이썬 단축평가 
            # 여기서 or 은 둘 중에 하나라도 True or 어떤값 = 무조건 앞의 True 반환 
            # next인자가 url에 없을때 -> None or 'articles:index '
            # False or T,F  = T,F 
            # 이런식으로 입력값에 따라 어디로 반환해주는지 설정할수있다.

    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'account_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
