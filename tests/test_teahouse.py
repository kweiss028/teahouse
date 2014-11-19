#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_teahouse
----------------------------------

Tests for `teahouse` module.
"""

import unittest

from teahouse import CoffeeMachine


def almost_equal(result_temp, expected_temp):    # tolerance for function slowness
    difference = expected_temp - result_temp
    return 0 <= difference <= 2


class TestTeahouse(unittest.TestCase):

    def setUp(self):
        self.teacup = CoffeeMachine.brew('tea')
        self.coffee_cup = CoffeeMachine.brew('coffee')
        self.bread_cup = CoffeeMachine.brew('bread')

    def test_has_attribute(self):
        self.assertTrue(hasattr(self.teacup, 'full'))
        self.assertFalse(hasattr(self.teacup, 'fill'))

    def test_wrong_drink(self):
        self.assertIsInstance(self.bread_cup, str)
        self.assertFalse(hasattr(self.bread_cup, 'price'))

    def test_right_drink(self):
        self.assertIsInstance(self.teacup, object)
        self.assertTrue(hasattr(self.teacup, 'price'))
        self.assertEqual(self.teacup.price, 1.80)
        
    def test_drink(self):
        self.teacup.drink(0.2)
        self.assertRaises(Exception, self.teacup.drink, -2)
        self.assertEqual(0.8, self.teacup.full)

    def test_heat_up(self):
        self.assertRaises(Exception, self.teacup.heat_up, -20)
        self.assertTrue(self.teacup.temp < 80)
        temp = self.teacup.temp
        self.teacup.heat_up(10)
        self.assertTrue(almost_equal(self.teacup.temp, temp + 10))    

    def test_has_timestamp(self):
        self.assertTrue(hasattr(self.teacup, '_timestamp'))

    def test_cool_down(self):    
        self.assertEqual(self.coffee_cup._init_temp, 80)
        self.coffee_cup._timestamp -= 1200    # set back start time by 20 minutes
        start_temp = self.coffee_cup.temp
        self.coffee_cup.heat_up(20)
        self.assertTrue(almost_equal(self.coffee_cup.temp, start_temp + 20))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
