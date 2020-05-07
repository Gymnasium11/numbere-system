import unittest
from calcNumbSys import *
from tkinter import *


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        root = Tk()
        self.window = Application(root)

    def test_ten_to_q(self):
        result = self.window.ten_to_q(15, 16)
        self.assertEqual(result, 'f')
        # self.assertEqual(self.window.ten_to_q(10,8), '12')


if __name__ == '__main__':
    unittest.main()
