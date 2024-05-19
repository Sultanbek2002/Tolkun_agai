from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Название категории")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    cover = models.ImageField(upload_to='book_covers/', verbose_name="Фото книги")
    categories = models.ManyToManyField(Category, related_name="books", verbose_name="Категории")
    
    def __str__(self):
        return self.title

class Topic(models.Model):
    name = models.CharField(max_length=200, verbose_name="Тема")
    books = models.ManyToManyField(Book, related_name="topics", verbose_name="Книги")
    
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",default='')
    content = RichTextField(verbose_name="Содержание")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="articles", verbose_name="Тема")
    
    def __str__(self):
        return self.title

class Proverd(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок",default='')
    content = RichTextField(verbose_name="Содержание")
    author=models.CharField(max_length=200, verbose_name="Автор рассказа")
    
    def __str__(self):
        return self.title
