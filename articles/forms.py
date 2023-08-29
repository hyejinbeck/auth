from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목입니다.',
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )

    # ModelForm은 모델을 알려주면 적용되는 기본모델을 알아서 폼제공해줌
    # 그럼 모델을 알려주기만 하면 된다 
    class Meta :
        model = Article 
        #fields = '__all__'
        exclude = ('user',)
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}), 
        #     'content': forms.Textarea(attrs={'class': 'form=control'}),
        # }
    