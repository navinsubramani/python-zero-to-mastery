import unittest
import main as program


class TestMain(unittest.TestCase):
    def test1_addition(self):
        '''This is a unit test program to test the additional function'''
        a = 4
        b = 2
        result = program.addition(a, b)
        self.assertEqual(result, 6)

    def test2_addition(self):
        a = 1
        b = 1
        result = program.addition(a, b)
        self.assertEqual(result, 2)


class TestGuessNumber(unittest.TestCase):

    def test1_guessnumber(self):
        self.assertEqual(program.guess_number(10, 10), True)

    def test2_guessnumber(self):
        self.assertEqual(program.guess_number(10, 9), False)

    def test3_guessnumber(self):
        self.assertEqual(program.guess_number(10, 'jack'), ValueError)

    def test4_guessnumber(self):
        self.assertEqual(program.guess_number(10, 13), False)


if __name__ == "__main__":
    unittest.main()
