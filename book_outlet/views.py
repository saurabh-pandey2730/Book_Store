from django.shortcuts import get_object_or_404 ,render
from .models import Book
from django.http import Http404
# Create your views here.

def index(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'book_outlet/index.html',{
        'books': books
    })
def book_detail(request,slug):
    # try:
    #      book =Book.objects.get(pk=id)
    # except:
    #     raise Http404('Book not found')
    book = get_object_or_404(Book,slug=slug)
    return render(request, 'book_outlet/book_detail.html',{
        'title':book.title,
        'author':book.author,
        'rating':book.rating,
        'is_bestseller':book.is_bestselling
        })