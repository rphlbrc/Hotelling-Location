import unittest
from hotelling import HotellingSimulator

class HotellingTest(unittest.TestCase):

    def testInitialize(self):
        hs = HotellingSimulator(20, 2)
        self.assertTrue(len(hs.scale) == 20)

    def testParse(self):
        hs = HotellingSimulator(10, 2)
        self.assertTrue(hs.parse("u 1 1 1") == 50.0)
        self.assertTrue(hs.parse("u 2 1 1") == 50.0)

    def testTwoCandidates(self):
        hs = HotellingSimulator(10, 2)
        self.assertTrue(hs.parse("u 1 2 8") == 45.0)
        self.assertTrue(hs.parse("u 2 2 8") == 55.0)
        self.assertTrue(hs.parse("u 1 8 9") == 80.0)
        self.assertTrue(hs.parse("u 2 8 9") == 20.0)

    def testDominance(self):
        hs = HotellingSimulator(10, 2)
        self.assertTrue(hs.parse("2 dominate? 1") == "strict")
        self.assertTrue(hs.parse("9 dominate? 10") == "strict")

if __name__ == '__main__':
    unittest.main()
