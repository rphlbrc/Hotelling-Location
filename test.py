import unittest
from hotelling import HotellingSimulator

class HotellingTest(unittest.TestCase):

	def testInitialize(self):
		hs = HotellingSimulator(20, 2)
		self.assertTrue(len(hs.scale) == 20)

	def testParse(self):
		hs = HotellingSimulator(10, 2)
		self.assertTrue(hs.parse("u 1 1 1") == 50.0)

if __name__ == '__main__':
	unittest.main()