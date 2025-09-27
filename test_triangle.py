

from unittest import TestCase

from triangle import Triangle, TrException


class TestTriangle(TestCase):
    def test_perimeter1(self):
        self.assertEqual(12, Triangle(3, 4, 5).perimeter())
        self.assertEqual(12, Triangle(4, 3, 5).perimeter())
        self.assertEqual(12, Triangle(5, 4, 3).perimeter())
    def test_perimeter2(self):
        self.assertEqual(27.6, Triangle(9.2, 9.2, 9.2).perimeter())

    def test_perimeter3(self):
        with self.assertRaises(TrException) as mes:
            trrr = Triangle(-3, 10, 10)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(10, -10, 10)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(10, 10, -10)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(0, 10, 10)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(10, 0, 10)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(10, 10, 0)
        self.assertEqual('отрицательная или нулевая длина стороны', str(mes.exception))

    def test_perimeter4(self):
        with self.assertRaises(TrException) as mes:
            trrr = Triangle(5, 5, 10)
        self.assertEqual('это не треугольник', str(mes.exception))

        with self.assertRaises(TrException) as mes:
            trrr = Triangle(10, 5, 5)
        self.assertEqual('это не треугольник', str(mes.exception))
