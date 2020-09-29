from django.urls import path
from . import views

urlpatterns = [
    path('get_books',views.get_books,name='get_books'),
    path('add_books',views.add_books,name='add_books'),
    path('delete_books',views.delete_books,name='delete_books'),
    path('update_books',views.update_books,name='update_books'),
    path('',views.index,name='index'),
]