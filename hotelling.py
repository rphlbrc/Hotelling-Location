import sys

class HotellingSimulator():

	def __init__(self, num, numPlayers):
		self.scale = [False for x in range(num)]
		self.numPlayers = numPlayers

	def parse(self, line):
		words = line.split()
		if words[0] == "u": # query for utility of player p
			p = int(words[1]) - 1
			pos = [-1 for x in range(self.numPlayers)]
			for i in range (self.numPlayers):
				pos[i] = int(words[i+2]) - 1

			return self.utility(p, pos)

	def utility(self, p, allPos):
		total = 0.0	
		for i in range(len(self.scale)):
			best = sys.maxint
			split = 0
			isP = False
			for j in range(len(allPos)):
				diff = abs(i - allPos[j])
				if diff < best:
					split = 1
					best = diff
					isP = (j == p)
				elif diff == best:
					split += 1
					isP = (j == p)
			if isP and split > 0: total += 10.0 / float(split)
		return total

			



def main():
	if (len(sys.argv) < 3): sys.exit()

	hs = HotellingSimulator(int(sys.argv[1]), int(sys.argv[2]))

	while 1:
		line = sys.stdin.readline()
		if not line: break
		print(hs.parse(line))


if __name__ == '__main__':
	main()