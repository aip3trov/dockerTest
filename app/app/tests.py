from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_sub_numbers(self):
        res = calc.sub(10, 5)

        self.assertEqual(res, 5)