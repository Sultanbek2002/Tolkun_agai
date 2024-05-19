import random
from django.shortcuts import render

from .models import *
# Create your views here.
kategory=Category.objects.all()

def index(request):
    all_books = list(Book.objects.all())
    # Перемешиваем книги
    random.shuffle(all_books)
    # Берем первые шесть книг после перемешивания
    featured_books = all_books[:6]
    context={
        "kategory": kategory,
        'featured_books': featured_books
    }
    return render(request,'website/other/index.html', context)

def proverd(request):
    proverds=Proverd.objects.all()
    context={
        "kategory": kategory,
        'proverds': proverds
    }
    return render(request, 'website/other/testimonials.html',context)

def book(request,id):
    books=Book.objects.filter(categories=id)
    context={
        "books": books,
        "kategory": kategory
    }
    return render(request, 'website/other/products.html',context)

def topic(request, id):
    topics=Topic.objects.filter(books=id)
    context={
        "topics": topics,
        "kategory": kategory
    }
    return render(request, 'website/other/blog.html',context)

def topic_detail(request, id):
    articles = Article.objects.filter(topic=id)
    topic = Topic.objects.get(id=id)
    books = Book.objects.filter(categories__in=topic.books.values_list('categories', flat=True)).distinct()
    print("after")
    for i in books:
        print(i.title)
    context = {
        "articles": articles,
        "kategory": kategory,
        "books": books
    }
    return render(request, 'website/other/product-details.html', context)

def checkout(request):
    context = {
        "kategory": kategory,
    }
    return render(request, 'website/other/checkout.html', context)

def contact(request):
    context = {
        "kategory": kategory,
    }
    return render(request, "website/other/contact.html", context)