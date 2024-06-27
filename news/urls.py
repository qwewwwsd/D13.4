from django.urls import path
from .views import (
   NewsPostList, NewsPostSearch, PostDetail, NewsPostCreate, NewsPostUpdate, NewsPostDelete
)
from news.views import (
   ArticleCreate, ArticleUpdate, ArticleDelete
)


urlpatterns = [
   path("", NewsPostList.as_view(), name="newspost_list"),
   path("<int:pk>", PostDetail.as_view(), name="newspost_detail"),
   path("search/", NewsPostSearch.as_view() ,name="newspost_search"),
   
   path("create/", NewsPostCreate.as_view(), name="newspost_create"),
   path("<int:pk>/update/", NewsPostUpdate.as_view(), name="newspost_update"),
   path("<int:pk>/delete/", NewsPostDelete.as_view(), name="product_delete"),
   
   path("articles/create/", ArticleCreate.as_view(), name="newspost_create"),
   path("articles/<int:pk>/update/", ArticleUpdate.as_view(), name="newspost_update"),
   path("articles/<int:pk>/delete/", ArticleDelete.as_view(), name="product_delete"),
]