from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, BookFriendList, BookFriendUpdate, FriendEdit
# from p_library import views

app_name = 'p_library'

urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('book_friend_list/', BookFriendList.as_view(), name='book_friend_list'),
    path('book_friend_update/<int:pk>', BookFriendUpdate.as_view(), name='book_friend_update'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
]