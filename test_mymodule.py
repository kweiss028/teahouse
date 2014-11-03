import unittest
from mymodule import Cup

teacup = Cup('tea', 1.80)
teaTime = int(teacup._timestamp)

coffee = Cup('coffee', 2.10)
coffeeTime = int(coffee._timestamp)

def almost_equal(resultTemp, expectedTemp):    # tolerance for function slowness
    difference = expectedTemp - resultTemp
    return (difference >= 0 and difference <= 2)



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
        self.assertTrue(teacup.temp < 80)
        temp = teacup.temp
        teacup.heat_up(10)
        self.assertTrue(almost_equal(teacup.temp, temp + 10))    

    def test_has_timestamp(self):
        self.assertTrue(hasattr(teacup, '_timestamp'))

    def test_cool_down(self):    
        self.assertEqual(coffee._init_temp, 80)
        coffee._timestamp -= 1200    # set back start time by 20 minutes
        startTemp = coffee.temp
        coffee.heat_up(20)
        self.assertTrue(almost_equal(coffee.temp, startTemp + 20))    



if __name__ == '__main__':
    unittest.main()