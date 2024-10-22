import unittest
from package.module1 import add


class TestModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3, add(1, 2))


if __name__ == "__main__":
    unittest.main()
