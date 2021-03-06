from binomial import Binomial
import unittest

class TestBinomialSingle(unittest.TestCase):
   def setUp(self):
       self.binomial = Binomial(1,-2,1)
   def test_real_roots(self):
       self.assertEqual(self.binomial.real_roots(), [1.0])
   def test_str(self):
       self.assertEqual(str(self.binomial),'1.0*x*x-2.0*x+1.0')

class  TestBinomialWithTwoRoots(unittest.TestCase):
   def setUp(self):
       self.binomial = Binomial(1,2,-3)
   def test_real_roots(self):
       self.assertEqual(self.binomial.real_roots(), [1.0,-3.0])
   def test_str(self):
       self.assertEqual(str(self.binomial),'1.0*x*x+2.0*x-3.0')

class TestWinomialWithoutRoots(unittest.TestCase):
   def setUp(self):
       self.binomial = Binomial(1,2,3)
   def test_real_roots(self):
       self.assertEqual(self.binomial.real_roots(), [])
   def test_str(self):
       self.assertEqual(str(self.binomial),'1.0*x*x+2.0*x+3.0')

class TestBinomialWithoutSecondCoefficient(unittest.TestCase):
   def setUp(self):
       self.binomial = Binomial(1,0,-4)
   def test_real_roots(self):
       self.assertEqual(self.binomial.real_roots(), [2.0,-2.0])
   def test_str(self):
       self.assertEqual(str(self.binomial),'1.0*x*x-4.0')

class TestBinomialWithoutThirdCoefficient(unittest.TestCase):
   def setUp(self):
       self.binomial = Binomial(1,2,0)
   def test_real_roots(self):
       self.assertEqual(self.binomial.real_roots(), [0.0,-2.0])
   def test_str(self):
       self.assertEqual(str(self.binomial),'1.0*x*x+2.0*x')

if __name__ == '__main__':
    unittest.main()

