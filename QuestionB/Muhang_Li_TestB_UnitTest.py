from Muhang_Li_testB import VersionComparor as vc
from unittest import TestCase


class MyTest(TestCase):
    def test_non_str(self):
        with self.assertRaises(AttributeError):
            vc.parse_version(123)
        with self.assertRaises(AttributeError):
            vc.parse_version(12.3)
        with self.assertRaises(AttributeError):
            vc.parse_version(True)


    def test_non_digit(self):
        with self.assertRaises(ValueError):
            vc.parse_version("1a.3")

    def test_negative_digit(self):
        with self.assertRaises(ValueError):
            vc.parse_version("1.-1")

    def test_with_space(self):
        self.assertEqual(vc.parse_version("1 . 3"), [1, 3])

    def test_samelength_lt(self):
        self.assertEqual(vc.less_than("1.1", "1.2"), True)
        self.assertEqual(vc.less_than("1.2", "1.1"), False)
        self.assertEqual(vc.less_than("1.1", "1.1"), False)

    def test_samelength_gt(self):
        self.assertEqual(vc.greater_than("1.1", "1.2"), False)
        self.assertEqual(vc.greater_than("1.1", "1.1"), False)
        self.assertEqual(vc.greater_than("1.2", "1.1"), True)


    def test_samelength_eq(self):
        self.assertEqual(vc.equals_to("1.1", "1.2"), False)
        self.assertEqual(vc.equals_to("1.2", "1.1"), False)
        self.assertEqual(vc.equals_to("1.1", "1.1"), True)

    def test_difflength_lt(self):
        self.assertEqual(vc.less_than("1.11", "1.2"), True)
        self.assertEqual(vc.less_than("1.21", "1.1"), False)
        self.assertEqual(vc.less_than("1.1", "1.21"), True)

    def test_difflength_gt(self):
        self.assertEqual(vc.greater_than("1.11", "1.2"), False)
        self.assertEqual(vc.greater_than("1.21", "1.1"), True)
        self.assertEqual(vc.greater_than("1.1", "1.21"), False)

    def test_difflength_eq(self):
        self.assertEqual(vc.equals_to("1.11", "1.2"), False)
        self.assertEqual(vc.equals_to("1.21", "1.1"), False)
        self.assertEqual(vc.equals_to("1.1", "1.21"), False)

    if __name__ == '__main__':
        import doctest
        doctest.testmod()

