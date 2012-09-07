import sys
from itertools import combinations_with_replacement

class HotellingSimulator():

    def __init__(self, num, numPlayers):
        self.scale = [False for x in range(num)]
        self.numPlayers = numPlayers

    def parse(self, line):
        words = line.split()
        if words[0] == "u": # query for utility of player p
            p = int(words[1]) - 1
            allPos = [-1 for x in range(self.numPlayers)]
            for i in range (self.numPlayers):
                allPos[i] = int(words[i+2]) - 1

            return str(self.utility(p, allPos))

        elif words[1] == "dominate?":
            s1 = int(words[0]) - 1
            s2 = int(words[2]) - 1

            return self.checkDominate(s1, s2)

    def utility(self, p, allPos):
        #print allPos
        total = 0.0 
        # TODO: there is a much faster linear algorithm for below, which is currently n^2  
        for i in range(len(self.scale)):
            best = sys.maxint
            bestC = -1
            split = 0
            for j in range(len(allPos)):
                diff = abs(i - allPos[j])
                if diff < best:
                    split = 1
                    best = diff
                    bestC = j
                elif diff == best:
                    split += 1
                    if j == p: bestC = j
            if bestC == p and split > 0: total += (100.0 / float(len(self.scale))) / float(split)
        return total

    def permute(self, numPlayers):
        master = []
        for i in range(len(self.scale)):
            master.append(i)

        output = combinations_with_replacement(master, numPlayers)
        return output

    def checkDominate(self, s1, s2):
        results = []

        opts = ["no", "weakly", "strictly"]

        for p in self.permute(self.numPlayers - 1):
            results.append(cmp(self.utility(0, [s1] + list(p)), self.utility(0, [s2] + list(p))))

        dominateOne = False
        dominateAll = True

        for r in results:
            if r < 0:
                dominateOne = False
                dominateAll = False
                break
            elif r == 0:
                dominateOne = True
                dominateAll = False
            else:
                dominateOne = True
                dominateAll = dominateAll and dominateOne

        return opts[int(dominateOne) + int(dominateAll)]

def main():
    if (len(sys.argv) < 3): sys.exit()

    hs = HotellingSimulator(int(sys.argv[1]), int(sys.argv[2]))

    while 1:
        line = sys.stdin.readline()
        if not line: break
        print(hs.parse(line))


if __name__ == '__main__':
    main()
