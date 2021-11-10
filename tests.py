from main import app
import unittest

class flasktest(unittest.TestCase):
    def test_if_true(self):
        value = 2
        self.assertEqual(value, 2)



if __name__ == '__main__':
    unittest.main()
