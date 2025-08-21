import unittest
from main import sum

class TestSuma(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(3, 5), 8)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(-5, -5), -10)

if __name__ == "__main__":
    unittest.main()