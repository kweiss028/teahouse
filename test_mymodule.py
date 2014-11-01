import unittest
import time
from mymodule import Cup

teacup = Cup('tea', 1.80)
teaTime = int(teacup.timestamp)

coffee = Cup('coffee', 2.10)
coffeeTime = int(coffee.timestamp)

class TestMyModule(unittest.TestCase):

    def test_has_attribute(self):
        self.assertTrue(hasattr(teacup, 'full'))
        self.assertFalse(hasattr(teacup, 'fill'))
    
    def test_drink(self):
        teacup.drink(0.2)
        self.assertRaises(Exception, teacup.drink, -2)
        self.assertEqual(0.8, teacup.full) 
        
    def test_heat_up(self):
        self.assertRaises(Exception, teacup.heat_up, -20)  
        self.assertEqual(teacup.temp, 80)
        teacup.timestamp = time.time()  # cup should not cool down before this test
        teacup.heat_up(10)
        self.assertEqual(teacup.temp, 90)     
    
    def test_has_timestamp(self):
        self.assertTrue(hasattr(teacup,'timestamp'))
    
    def test_cool_down(self):       # some tolerance for timer problems
        self.assertEqual(coffee.temp, 80)
        time.sleep(2)
        startTemp = coffee.get_temp()
        self.assertTrue(startTemp < 80)
        coffee.heat_up(20)
        time.sleep(2)
        endTemp = coffee.get_temp()        
        self.assertTrue(endTemp > startTemp)
        self.assertTrue(endTemp < startTemp + 20)
        
          
if __name__ == '__main__':
    unittest.main()