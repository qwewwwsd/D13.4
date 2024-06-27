from django import forms
from django.core.exceptions import ValidationError

from .models import NewsPost
from .templatetags.censor import censor_list

class NewsPostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    title = forms.CharField(max_length=50)
    
    class Meta:
        model = NewsPost
        fields = [
           "title",
           "text",
           "category",
       ]
    
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        title = str(title)
        text = str(text)
        for dd in [title, text]:
            for i in dd.split():
                for a in censor_list:
                    if i == a:
                        raise ValidationError(
                            "В тексте содержится нецензурная брань!"
                        )

        return cleaned_data


class ArticlesForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    title = forms.CharField(max_length=50)
    
    class Meta:
        model = NewsPost
        fields = [
           "title",
           "text",
           "category",
       ]
    
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        title = str(title)
        text = str(text)
        for dd in [title, text]:
            for i in dd.split():
                for a in censor_list:
                    if i == a:
                        raise ValidationError(
                            "В тексте содержится нецензурная брань!"
                        )

        return cleaned_data