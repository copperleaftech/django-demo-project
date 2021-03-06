from django.contrib import admin

from reversion.admin import VersionAdmin

from import_export.admin import ImportExportMixin

from .models import Category, Book, Author


class CategoryAdmin(ImportExportMixin, VersionAdmin, admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class BookAdmin(ImportExportMixin, VersionAdmin, admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class AuthorAdmin(ImportExportMixin, VersionAdmin, admin.ModelAdmin):
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
