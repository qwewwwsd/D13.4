from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.views.decorators.csrf import csrf_protect

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import NewsPost, Category, Subscription
from .filters import PostFilter
from .forms import NewsPostForm, ArticlesForm


# Create your views here.
class NewsPostList(ListView):
    model = NewsPost
    ordering = "-dateCreation"
    template_name = "newsPost.html"
    context_object_name = "newss"
    paginate_by = 10
    

class NewsPostSearch(ListView):
    model = NewsPost
    ordering = "-dateCreation"
    template_name = "newsPost_search.html"
    context_object_name = "newss"
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["filterset"] = self.filterset
       return context


class PostDetail(DetailView):
    model = NewsPost
    template_name = "newsPost_one.html"
    context_object_name = "newss"


class NewsPostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.newspost_edit',)
    raise_exception = True
    form_class = NewsPostForm
    model = NewsPost
    template_name = "newspost_edit.html"
    

class ArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.article_edit',)
    raise_exception = True
    form_class = ArticlesForm
    model = NewsPost
    template_name = "article_edit.html"
    

class NewsPostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.newspost_edit',)
    raise_exception = True
    form_class = NewsPostForm
    model = NewsPost
    template_name = "newspost_edit.html"


class ArticleUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.article_edit',)
    raise_exception = True
    form_class = ArticlesForm
    model = NewsPost
    template_name = "article_edit.html"


class NewsPostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.newspost_delete',)
    raise_exception = True
    model = NewsPost
    template_name = "newspost_delete.html"
    success_url = reverse_lazy("newspost_list")


class ArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.article_delete',)
    raise_exception = True
    model = ArticlesForm
    template_name = "article_delete.html"
    success_url = reverse_lazy("newspost_list")


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )