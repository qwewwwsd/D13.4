from django.urls import path
from .views import (
   NewsPostList, NewsPostSearch, PostDetail, NewsPostCreate, NewsPostUpdate, NewsPostDelete
)
from news.views import (
   ArticleCreate, ArticleUpdate, ArticleDelete
)

from django.views.decorators.cache import cache_page


urlpatterns = [
   path("", cache_page(60*5)(NewsPostList.as_view()), name="newspost_list"),
   path("<int:pk>", cache_page(60)(PostDetail.as_view()), name="newspost_detail"),
   path("search/", cache_page(60*5)(NewsPostSearch.as_view()) ,name="newspost_search"),
   
   path("create/", cache_page(60*5)(NewsPostCreate.as_view()), name="newspost_create"),
   path("<int:pk>/update/", cache_page(60*5)(NewsPostUpdate.as_view()), name="newspost_update"),
   path("<int:pk>/delete/", cache_page(60*5)(NewsPostDelete.as_view()), name="product_delete"),
   
   path("articles/create/", cache_page(60*5)(ArticleCreate.as_view()), name="newspost_create"),
   path("articles/<int:pk>/update/", cache_page(60*5)(ArticleUpdate.as_view()), name="newspost_update"),
   path("articles/<int:pk>/delete/", cache_page(60*5)(ArticleDelete.as_view()), name="product_delete"),
]