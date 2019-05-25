
import unittest
import os 

class SimplisticTest(unittest.TestCase):

    def test(self):
        print(os.environ.get("ctf"))
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
