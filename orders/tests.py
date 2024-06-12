from django.contrib.auth import get_user_model
from django.test import TestCase

from orders.models import Order

# Create your tests here.

User = get_user_model()

# class UserTestCase(TestCase):
#     def setUp(self):
#         self.user_a = User.objects.create(username='ali',password= '1234')
        
#     def test_user_count(self):
#         self.assertEqual(1,User.objects.count())
        
#     def test_user_pw(self):
#         self.assertTrue(self.user_a.check_password('1234'))

class OrderTestCase(TestCase):
    def setUp(self):
            self.user_a = User.objects.create(username='ali',password= '1234')    
            self.order_a = Order.objects.create(user=self.user_a,status = 'mmd',payment_method='dddd')
    
    def test_orders(self):
        qs =self.order_a.orderItem_set.all()
        print('-----')
        self.assertEqual(qs.count(),0)
    
        
        
