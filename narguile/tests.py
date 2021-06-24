from django.test import TestCase
import pytest

from .models import Product


@pytest.mark.usefixtures(
    'make_product',
    'make_category'
    )
class TestProduct(TestCase):

    
    def test_class_product_exist(self):

        self.assertIsInstance(self.fake_product, Product)

    

    # Exemplo de Mock
    #  
    # @patch('narguile.models.validate_str')
    # def test_method_create(self,validate_str_mock):
        
    #     validate_str_mock.return_value = []

    #     product = create_product(            
    #         name=1,
    #         description='DescriptionTest',
    #         price=250.00,
    #         category=build_category()
    #         )

    #     self.assertEqual(product.name, 1)
    