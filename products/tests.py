from django.test import TestCase
import os
from dotenv import load_dotenv

# Create your tests here.
class ProductTestCase(TestCase):
    def test_is_equal(self):
        load_dotenv()
        test_case = os.environ.get('TEST_CASE')
        self.assertEqual(test_case,'123')
        self.assertGreaterEqual(2,1)
        self.assertEqual(1,1)
        self.assertFalse(1,2)
        