from django.contrib import admin

from .models import Category, Book, Author


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'email')
    list_display = ('name', 'email')
    list_editable = ('email',)
    search_fields = ('name', 'email')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = self.readonly_fields
        if obj:
            readonly_fields += ('name',)
        return readonly_fields


admin.site.register(Author, AuthorAdmin)
