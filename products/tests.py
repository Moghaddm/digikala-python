from django.test import TestCase
import os
from dotenv import load_dotenv

from .models import Product
from django.utils.text import slugify

# Create your tests here.
class ProductTestCase(TestCase):
    
    def setUp(self):
        Product.products.create(name = 'short',description = 'simple description',price= 12000)
                
    def test_queryset_count(self):
        obj =Product.products.order_by('id').get(pk = 1)
        self.assertEqual(obj.slug,slugify(obj.name))
        
    def test_is_equal(self):
        load_dotenv()
        test_case = os.environ.get('TEST_CASE')
        self.assertEqual(test_case,'123')
        
    def test_update_product(self):
        obj = Product.products.get(pk=1)
        obj.name = 'mobile'
        obj.save()
        self.assertEqual(obj.name,'mobile')
        
    def test_search_product(self):
        queryset = Product.products.search('short')
        self.assertEqual(len(queryset),1)
        
        