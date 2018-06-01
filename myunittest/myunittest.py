import unittest
import ericmath

class ProductTestCase(unittest.TestCase):
    def setUp(self):

        pass
    def testinterger(self):
        for x in range(-10,10):
            for y in range(-10,10):
                p=ericmath.square1(x, y)
                self.assertTrue(p==x*y,"Error")
    def testfloat(self):
        for x in range(-10,10):
            for y in range(-10,10):
                x=x/10.0
                y=y/10.0
                p=ericmath.square1(x, y)
        self.assertTrue(p==x*y,"2Error")
    def tearDown(self):
        print("downdown")
        pass
if __name__ == '__main__':
    unittest.main()
    print("1-111")



