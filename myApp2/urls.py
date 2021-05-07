from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('create', views.create),
    path('signin', views.signin),
    path('logout', views.logout),
    path('books/add', views.booksadd),
    path('books/create', views.bookCreate),
    path('books/<str:id>', views.bookView),
    path('books/<str:id>/addReview', views.addReview),
    path('user/<str:id>', views.user),
    
]
