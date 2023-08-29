from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # ModelForm은 모델을 알려주면 적용되는 기본모델을 알아서 폼제공해줌
    # 그럼 모델을 알려주기만 하면 된다 
    class Meta :
        model = Article 
        #fields = '__all__'
        exclude = ('user',)
    