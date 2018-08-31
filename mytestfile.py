import unittest
#from unnecessary_math import multiply
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( 3*4, 12)

    def test_numbers_4_4(self):
        self.assertEqual( 4*7, 28)

    def test_numbers_5_4(self):
        self.assertEqual( 5*4, 20) 


    def test_strings_a_3(self):
        self.assertEqual('a'*3, 'aaa')
 
if __name__ == '__main__':
    unittest.main()
