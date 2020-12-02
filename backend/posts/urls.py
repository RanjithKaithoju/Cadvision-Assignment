from django.urls import path,re_path
from .views import posts,comments,postlike,postdislike,index
urlpatterns=[
    path('posts/',posts.as_view()),
    path('comments/',comments.as_view()),
    re_path(r'^post/like/(?P<pk>\d+)/$', # Like
        postlike.as_view(),
        name='post_like'
    ),
    re_path(r'^post/dislike/(?P<pk>\d+)/$', # DisLike
        postdislike.as_view(),
        name='post_dislike'
    ),
    path('',index)
]