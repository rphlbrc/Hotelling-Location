import sys

class HotellingSimulator():

	def __init__(self, num, numPlayers):
		self.scale = [False for x in range(num)]
		self.numPlayers = numPlayers

	def parse(self, line):
		words = line.split()
		if words[0] == "u":
			return 50.0


def main():
	if (len(sys.argv) < 3): sys.exit()

	hs = HotellingSimulator(int(sys.argv[1]), int(sys.argv[2]))

	for line in sys.stdin:
		hs.parse(line)

if __name__ == '__main__':
	main()