from django.urls import path
# from .views import books_detail, books_list
from .views import BooksListView, BookCreateView, BookDetailView, BookUpdateView, BookDeleteView, AuthorCreateView, AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView

app_name = 'library'

urlpatterns = [
    path('', AuthorListView.as_view(), name='home'),
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='books_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:pk>/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
    # path('books_list/', books_list, name='books_list'),
    # path('books_detail/<int:book_id>', books_detail, name='books_detail'),

]
