from django.contrib import admin

from .models import Category, Book, Author


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
