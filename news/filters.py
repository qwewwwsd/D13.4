from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from django.forms import DateTimeInput
from django_filters import FilterSet
from .models import NewsPost, Category

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name="dateCreation",
        lookup_expr="gt",
        label='Поиск позже указываемой даты',
        widget=DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={"type": "datetime-local"},
        ),
    )
    
    title = CharFilter(
		field_name='title',
		lookup_expr='icontains',
		label='Поиск по заголовку',
    )
    
    category = ModelChoiceFilter(
		field_name='category',
		queryset=Category.objects.all(),
		label='Категория',
		empty_label='Выберите категорию',
	)

    class Meta:
       model = NewsPost
       fields = {}
       