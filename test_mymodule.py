import unittest
from mymodule import CoffeeMachine

teacup = CoffeeMachine('tea').product
coffee_cup = CoffeeMachine('coffee').product
bread_cup = CoffeeMachine('bread').product


def almost_equal(result_temp, expected_temp):    # tolerance for function slowness
    difference = expected_temp - result_temp
    return 0 <= difference <= 2


class TestMyModule(unittest.TestCase):

    def test_has_attribute(self):
        self.assertTrue(hasattr(teacup, 'full'))
        self.assertFalse(hasattr(teacup, 'fill'))

    def test_wrong_drink(self):
        self.assertIsInstance(bread_cup, str)
        self.assertFalse(hasattr(bread_cup, 'price'))

    def test_right_drink(self):
        self.assertIsInstance(teacup, object)
        self.assertTrue(hasattr(teacup, 'price'))
        self.assertEqual(teacup.price, CoffeeMachine._price_list['tea'])
        
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
        self.assertEqual(coffee_cup._init_temp, 80)
        coffee_cup._timestamp -= 1200    # set back start time by 20 minutes
        start_temp = coffee_cup.temp
        coffee_cup.heat_up(20)
        self.assertTrue(almost_equal(coffee_cup.temp, start_temp + 20))


if __name__ == '__main__':
    unittest.main()