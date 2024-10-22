from django.urls import path
# from .views import books_detail, books_list
from .views import BooksListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

app_name = 'library'

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    # path('books_list/', books_list, name='books_list'),
    # path('books_detail/<int:book_id>', books_detail, name='books_detail'),

]
