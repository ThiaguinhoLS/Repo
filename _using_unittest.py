# -*- coding: utf-8 -*-
import unittest


def fat(x):
    value = 1
    for i in range(1, x+1):
        value *= i
    return value


class TestFatFunc(unittest.TestCase):

    def test_fat_func_with_arg_zero(self):
        value = fat(0)
        self.assertEqual(value, 0)


if __name__ == '__main__':
    unittest.main()
