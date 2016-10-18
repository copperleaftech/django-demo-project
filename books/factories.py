import factory

from django.utils.text import slugify

from .models import Category, Book, Author

from faker import Faker
fake = Faker()


class AuthorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Faker('name')
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(slugify(a.name)).lower())


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')


class BookFactory(factory.DjangoModelFactory):
    class Meta:
        model = Book
        django_get_or_create = ('isbn',)

    name = factory.Faker('sentence')
    isbn = factory.Faker('ean13')
    author = factory.SubFactory(AuthorFactory)

    @factory.post_generation
    def categories(self, create, count=None, **kwargs):
        make_category = getattr(CategoryFactory, 'create' if create else 'build')

        if count:
            categories = [make_category() for i in range(count)]
            for category in categories:
                self.categories.add(category)
