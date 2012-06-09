from binomial import Binomial
import unittest

class TestBenomial(unittest.TestCase):
   def setUp(self):
       self.a=1
       self.b=-2
       self.c=1
   def test_real_roots(self):
       self.assertEqual(Binomial(self.a,self.b,self.c).real_roots(), [1.0])
   def test_str(self):
       self.assertEqual(str(Binomial(self.a,self.b,self.c)),'1.0*x*x-2.0*x+1.0')
if __name__ == '__main__':
    unittest.main()
