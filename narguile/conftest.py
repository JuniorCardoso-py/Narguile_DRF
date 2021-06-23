from narguile.models import Category, Product
from _pytest.fixtures import fixture


def build_category():
    return Category(name='Pequena')

@fixture
def make_product(request):
    product = Product(
            name='TesteName',
            description='DescriptionTest',
            price=250.00,
            category=build_category()
            )
    request.cls.fake_product = product
    return request

@fixture
def make_category(request):
    category = Category(name="Pequena")
    request.cls.fake_category = category
    return request

